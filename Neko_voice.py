import os.path
import sqlite_Neko
import subprocess
import Neko_layout
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pyttsx3
import speech_recognition
import webbrowser
import wave
import json
from vosk import Model, KaldiRecognizer
import keyboard


def voice_helper():
	while True:
		commands = {
			(f"до встречи", f"пока", f"закончить работу", f"завершение", f"на этом всё", f"выключение",
			 f"прекращение", f"выключайся", f"off", f"не работай",
			 f"больше не работай"): play_farewell_and_quit,
			(f"гугл", f"найди", f"google", f"поиск", f"открой гугл", f"открыть гугл", f"найти в гугл",
			 f"найти", f"найти в гугле", f"найти в google", f"загугли", f"загуглить", f"поискать",
			 f"ищем"): search_for_term_on_google,
			(f"ютуб", f"видео", f"youtube", f"на ютубе", f"найти видео", f"искать видео", f"искать на ютуб",
			 f"искать на youtube", f"в ютубе"): search_for_video_on_youtube,
			(f"википедия", f"вики", f"wikipedia", f"энциклопедия", f"расскажи о", f"википедии", f"в википедии",
			 f"википедию", f"открой википедию"): search_for_definition_on_wikipedia,
			(f"копируй", f"копируйте", f"скопируй", f"копирую"): copy_data,
			(f"вставить", f"вставь", f"ставь", f"ставить"): input_copied_data,
			(f"помоги", f"диспетчер", f"помощник", f"диспетчер", f"диспетчер"): dispatcher,
			(f"вырезать", f"вырезать", f"вырезать", f"вырезать", f"вырезать"): cut_data,
			(f"команда", f"голосовая",f"выполнить", f"используй", f"примени", f"сделай"): active_command_voice
		}
		voice_input = record_and_recognize_audio()
		if os.path.exists("microphone-results.wav"):
			os.remove("microphone-results.wav")
			print(voice_input)
			voice_input = voice_input.split(" ")
			conn = sqlite_Neko.create_connection("Neko.db")
			with conn:
				character_name = sqlite_Neko.get_name(conn)
			if len(voice_input) > 1:
				helper_name = voice_input[0]
				if fuzz.ratio(helper_name, character_name) > 20:
					command = voice_input[1]
					if len(voice_input) > 2:
						command_options = [str(input_part) for input_part in voice_input[2:len(voice_input)]]
						execute_command_with_name(command, commands, command_options)
					else:
						command_options = ["none"]
						execute_command_with_name(command, commands, command_options)
				else:
					voice_helper()
			else:
				voice_helper()


def execute_command_with_name(command_name: str, dictionary: dict, *args: list):
	"""
	Выполнение заданной пользователем команды и аргументами
	:param command_name: название команды
	:param args: аргументы, которые будут переданы в метод
	:param dictionary: словарь с функциями
	:return:
	"""
	if command_name:
		for key in dictionary.keys():
			for i in range(len(key)):
				if fuzz.ratio(command_name, key[i]) > 70:
					dictionary[key](*args)
			else:
				print("Command not found")
	else:
		voice_helper()



def record_and_recognize_audio():
	"""
	Запись и распознавание аудио
	"""
	microphone = speech_recognition.Microphone()
	recognizer = speech_recognition.Recognizer()

	with microphone:
		recognized_data = ""

		# регулирование уровня окружающего шума
		recognizer.adjust_for_ambient_noise(microphone, duration=2)

		try:
			print("Listening...")
			audio = recognizer.listen(microphone, 5, 5)

			with open("microphone-results.wav", "wb") as file:
				file.write(audio.get_wav_data())

		except speech_recognition.WaitTimeoutError:
			print("Can you check if your microphone is on, please?")
			return

		# использование online-распознавания через Google
		try:
			print("Started recognition...")
			conn = sqlite_Neko.create_connection("Neko.db")
			with conn:
				language = sqlite_Neko.get_language(conn)
				if language == "russian":
					recognized_data = recognizer.recognize_google(audio, language="ru").lower()
				elif language == "english":
					recognized_data = recognizer.recognize_google(audio, language="en").lower()

		except speech_recognition.UnknownValueError:
			pass

		except speech_recognition.RequestError:
			print("Trying to use offline recognition...")
			recognized_data = use_offline_recognition()
			print(recognized_data)
	return recognized_data


def use_offline_recognition():
	recognized_data = ""
	try:
		if not os.path.exists("vosk-model-small-ru-0.22"):
			print("Please download the model from:\n"
			      "https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
			exit(1)

		wave_audio_file = wave.open("microphone-results.wav", "rb")
		model = Model("vosk-model-small-ru-0.22")
		offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())
		data = wave_audio_file.readframes(wave_audio_file.getnframes())
		if data:
			if offline_recognizer.AcceptWaveform(data):
				recognized_data = offline_recognizer.Result()
				recognized_data = json.loads(recognized_data)
				recognized_data = recognized_data["text"]
	except:
		print("Sorry, speech service is unavailable. Try again later")
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


def search_for_definition_on_wikipedia(*args: tuple):
	"""
	Поиск в Wikipedia определения с последующим озвучиванием результатов и открытием ссылок
	:param args: фраза поискового запроса
	"""
	if not args[0]: return
	search_term = " ".join(args[0])
	url = "https://ru.wikipedia.org/wiki/" + search_term
	webbrowser.get().open(url)


def play_farewell_and_quit(*args: tuple):
	"""
	Проигрывание прощательной речи и выход
	"""
	ttsEngine = pyttsx3.init()
	ttsEngine.stop()
	quit()


def copy_data(*args: tuple):
	keyboard.press("ctrl")
	keyboard.press("c")
	keyboard.release("c")
	keyboard.release("ctrl")


def cut_data(*args: tuple):
	keyboard.press("ctrl")
	keyboard.press("x")
	keyboard.release("x")
	keyboard.release("ctrl")


def input_copied_data(*args: tuple):
	keyboard.press("ctrl")
	keyboard.press("v")
	keyboard.release("ctrl")
	keyboard.release("v")


def dispatcher(*args: tuple):
	keyboard.press("ctrl")
	keyboard.press("shift")
	keyboard.press("esc")
	keyboard.release("ctrl")
	keyboard.release("shift")
	keyboard.release("esc")


def active_command_voice(button_name):
	"""считывает название кнопки, выполняет команду"""
	conn = sqlite_Neko.create_connection("Neko.db")
	with conn:
		sql_command_name = sqlite_Neko.voice_commands_names(conn)
		sql_command_name_source = sqlite_Neko.voice_commands_source(conn)
		sql_command_status = sqlite_Neko.voice_commands_status(conn)
		print(sql_command_name)
		print(sql_command_name_source)
		print(sql_command_status)
		main_button_name = str()
		for i in range(len(button_name)):
			if i < len(button_name) - 1:
				main_button_name = main_button_name + str(button_name[i]) + ' '
			elif i == len(button_name) - 1:
				main_button_name = main_button_name + str(button_name[i])
		for i in range(len(sql_command_name)):
			if fuzz.ratio(str(main_button_name), sql_command_name[i]) > 70:
				index = sql_command_name.index(str(main_button_name))
				real_name = sql_command_name_source[index]
				status = sql_command_status[index]
				if int(status) == 1:
					sql_command_type = sqlite_Neko.select_type_of_commands(conn)
					sql_command_files = sqlite_Neko.select_files_of_commands(conn)
					sql_command_site = sqlite_Neko.select_sites_of_command(conn)
					index = sql_command_name.index(str(real_name))
					command_type = sql_command_type[index]
					if command_type == 's':
						if sql_command_site[index].find("https://"):
							webbrowser.open_new_tab(str(sql_command_site[index]))
						else:
							webbrowser.open_new_tab("https://" + str(sql_command_site[index]))
					elif command_type == 'f':
						for i in sql_command_files[index]:
							print(sql_command_files[index])
							if os.path.exists(i) is True:
								subprocess.call(('cmd', '/c', 'start', '', i))
							elif os.path.exists(i) is False:
								if i == "":
									pass


def show_voice_settings(self):
	self.voice_set_1.show()


def close_voice_settings(self):
	self.voice_set_1.hide()
