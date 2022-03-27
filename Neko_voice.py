    def play_voice_assistant_speech(self, text_to_speech):
        """
        Проигрывание речи ответов голосового ассистента (без сохранения аудио)
        :param text_to_speech: текст, который нужно преобразовать в речь
        """
        ttsEngine.say(str(text_to_speech))
        ttsEngine.runAndWait()

# Часть с голосовым помощником
    def record_and_recognize_audio(self, *args: tuple):
        """
        Запись и распознавание аудио
        """
        with microphone:
            recognized_data = ""

            # регулирование уровня окружающего шума
            recognizer.adjust_for_ambient_noise(microphone, duration=2)

            try:
                print("Listening...")
                audio = recognizer.listen(microphone, 25, 25)

                with open("microphone-results.wav", "wb") as file:
                    file.write(audio.get_wav_data())

            except speech_recognition.WaitTimeoutError:
                print("Can you check if your microphone is on, please?")
                return

            # использование online-распознавания через Google
            try:
                print("Started recognition...")
                recognized_data = recognizer.recognize_google(audio, language="ru").lower()

            except speech_recognition.UnknownValueError:
                pass

            # в случае проблем с доступом в Интернет происходит попытка
            # использовать offline-распознавание через Vosk
            except speech_recognition.RequestError:
                print("Trying to use offline recognition...")
        return recognized_data

    def search_for_term_on_google(self, *args: tuple):
        """
        Поиск в Google с автоматическим открытием ссылок (на список результатов и на сами результаты, если возможно)
        :param args: фраза поискового запроса
        """
        if not args[0]: return
        search_term = " ".join(args[0])

        # открытие ссылки на поисковик в браузере
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)

    def search_for_video_on_youtube(self, *args: tuple):
        """
        Поиск видео на YouTube с автоматическим открытием ссылки на список результатов
        :param args: фраза поискового запроса
        """
        if not args[0]: return
        search_term = " ".join(args[0])
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        self.play_voice_assistant_speech(f"Вот что было найдено по запросу {search_term}")

    def search_for_definition_on_wikipedia(self, *args: tuple):
        """
        Поиск в Wikipedia определения с последующим озвучиванием результатов и открытием ссылок
        :param args: фраза поискового запроса
        """
        if not args[0]: return

        search_term = " ".join(args[0])

        wiki = wikipediaapi.Wikipedia("ru-RU")

        wiki_page = wiki.page(search_term)
        try:
            if wiki_page.exists():
                self.play_voice_assistant_speech(f"Вот что было найдено по запросу {search_term} на Википедии")
                webbrowser.get().open(wiki_page.fullurl)
                self.play_voice_assistant_speech(wiki_page.summary.split(".")[:2])
            else:
                # открытие ссылки на поисковик в браузере в случае, если на Wikipedia не удалось найти ничего по запросу
                self.play_voice_assistant_speech(f"{search_term} не найдена на Википедии. Вот в гугл")
                url = "https://google.com/search?q=" + search_term
                webbrowser.get().open(url)
        except:
            self.play_voice_assistant_speech("Проблема с доступом")
            traceback.print_exc()
            return

    def play_greetings(self, *args: tuple):
        """
        Проигрывание случайной приветственной речи
        """
        greetings = ["Привет", "Здравствуй"]
        self.play_voice_assistant_speech(greetings[random.randint(0, len(greetings)-1)])

    def play_farewell_and_quit(self, *args: tuple):
        """
        Проигрывание прощательной речи и выход
        """
        farewells = ["Пока", "До новых встреч"]
        self.play_voice_assistant_speech(farewells[random.randint(0, len(farewells) - 1)])
        ttsEngine.stop()
        quit()

    def execute_command_with_name(self, command_name: str, *args: list):
        """
        Выполнение заданной пользователем команды и аргументами
        :param command_name: название команды
        :param args: аргументы, которые будут переданы в метод
        :return:
        """
        for key in self.commands.keys():
            if command_name in key:
                self.commands[key](*args)
            else:
                print("Command not found")

        def voice_helper():
            voice_input = self.record_and_recognize_audio()
            os.remove("microphone-results.wav")
            print(voice_input)
            voice_input = voice_input.split(" ")
            command = voice_input[0]
            command_options = [str(input_part) for input_part in voice_input[1:len(voice_input)]]
            self.execute_command_with_name(command, command_options)