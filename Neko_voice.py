import apiai
import json
import re
import pyttsx3
import speech_recognition
import webbrowser
import wikipediaapi
import wave
import os
import traceback
import random

ttsEngine = pyttsx3.init()
rate = ttsEngine.getProperty('rate')
ttsEngine.setProperty('rate', 140)
volume = ttsEngine.getProperty('volume')
ttsEngine.setProperty('volume', 3)
voices = ttsEngine.getProperty('voices')
ttsEngine.setProperty('voice', 'ru')
ttsEngine.setProperty('voice', 'Anna')


def record_and_recognize_audio(*args: tuple):
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


def search_for_term_on_google(*args: tuple):
    """
    Поиск в Google с автоматическим открытием ссылок (на список результатов и на сами результаты, если возможно)
    :param args: фраза поискового запроса
    """
    if not args[0]: return
    search_term = " ".join(args[0])

    # открытие ссылки на поисковик в браузере
    url = "https://google.com/search?q=" + search_term
    webbrowser.get().open(url)


def search_for_video_on_youtube(*args: tuple):
    """
    Поиск видео на YouTube с автоматическим открытием ссылки на список результатов
    :param args: фраза поискового запроса
    """
    if not args[0]: return
    search_term = " ".join(args[0])
    url = "https://www.youtube.com/results?search_query=" + search_term
    webbrowser.get().open(url)
    play_voice_assistant_speech(f"Вот что было найдено по запросу {search_term}")


def search_for_definition_on_wikipedia(*args: tuple):
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
            play_voice_assistant_speech(f"Вот что было найдено по запросу {search_term} на Википедии")
            webbrowser.get().open(wiki_page.fullurl)
            play_voice_assistant_speech(wiki_page.summary.split(".")[:2])
        else:
            # открытие ссылки на поисковик в браузере в случае, если на Wikipedia не удалось найти ничего по запросу
            play_voice_assistant_speech(f"{search_term} не найдена на Википедии. Вот в гугл")
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
    except:
        play_voice_assistant_speech("Проблема с доступом")
        traceback.print_exc()
        return


def play_greetings(*args: tuple):
    """
    Проигрывание случайной приветственной речи
    """
    greetings = ["Привет", "Здравствуй"]
    play_voice_assistant_speech(greetings[random.randint(0, len(greetings)-1)])


def play_farewell_and_quit(*args: tuple):
    """
    Проигрывание прощательной речи и выход
    """
    farewells = ["Пока", "До новых встреч"]
    play_voice_assistant_speech(farewells[random.randint(0, len(farewells) - 1)])
    ttsEngine.stop()
    quit()


def execute_command_with_name(command_name: str, *args: list):
    """
    Выполнение заданной пользователем команды и аргументами
    :param command_name: название команды
    :param args: аргументы, которые будут переданы в метод
    :return:
    """
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
        else:
            pass  # print("Command not found")


# перечень команд для использования (качестве ключей словаря используется hashable-тип tuple)
# в качестве альтернативы можно использовать JSON-объект с намерениями и сценариями
# (подобно тем, что применяют для чат-ботов)
commands = {
    ("hello", "hi", "morning", "привет"): play_greetings,
    ("bye", "goodbye", "quit", "exit", "stop", "пока"): play_farewell_and_quit,
    ("search", "google", "find", "найди"): search_for_term_on_google,
    ("video", "youtube", "watch", "видео"): search_for_video_on_youtube,
    ("wikipedia", "definition", "about", "определение", "википедия"): search_for_definition_on_wikipedia,
}


def play_voice_assistant_speech(text_to_speech):
    """
    Проигрывание речи ответов голосового ассистента (без сохранения аудио)
    :param text_to_speech: текст, который нужно преобразовать в речь
    """
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()


if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()
    while True:
        a = record_and_recognize_audio()
        play_voice_assistant_speech(a)
