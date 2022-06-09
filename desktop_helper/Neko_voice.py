import os
import sounddevice as sd
import subprocess
import webbrowser
from PyQt5 import QtCore, QtWidgets
import vosk
import sys
from fuzzywuzzy import fuzz
import queue
import json
from desktop_helper import sqlite_Neko
import threading


# def active_command_button(button_name):
#     """считывает название кнопки, выполняет команду"""
#     conn = sqlite_Neko.create_connection("Neko.db")
#     with conn:
#         sql_command_name = sqlite_Neko.select_all_command(conn)
#         sql_command_type = sqlite_Neko.select_type_of_commands(conn)
#         sql_command_files = sqlite_Neko.select_files_of_commands(conn)
#         sql_command_site = sqlite_Neko.select_sites_of_command(conn)
#         index = sql_command_name.index(button_name)
#         command_type = sql_command_type[index]
#         if command_type == 's':
#             if sql_command_site[index].find("https://"):
#                 webbrowser.open_new_tab(str(sql_command_site[index]))
#             else:
#                 webbrowser.open_new_tab("https://" + str(sql_command_site[index]))
#         elif command_type == 'f':
#             for i in sql_command_files[index]:
#                 print(sql_command_files[index])
#                 if os.path.exists(i) is True:
#                     subprocess.call(('cmd', '/c', 'start', '', i))
#                 elif os.path.exists(i) is False:
#                     pass
#
#
# Neko_setup = Voice_setup()
# Neko_setup.append_command_to_default()
# q = queue.Queue()
#
#
# def va_respond(voice: str):
#     print("[Text]: ", voice)
#     if Neko_setup.name_character != "":
#         voice_input = voice.split(" ", 1)
#         if len(voice_input) > 1:
#             if fuzz.ratio(voice_input[0], Neko_setup.name_character) >= 20:
#                 print("--[Overlap]--:", voice_input[0], " - - ", Neko_setup.name_character)
#                 for key in Neko_setup.commands:
#                     for item in Neko_setup.commands[key]:
#                         if fuzz.ratio(voice_input[1], item) >= 70:
#                             active_command_button(key)
#             else:
#                 print("//Unexpected name character")
#     else:
#         for key in Neko_setup.commands:
#             for item in Neko_setup.commands[key]:
#                 if fuzz.ratio(voice, item) >= 80:
#                     active_command_button(key)
#
#
# def q_callback(indata, frames, time, status):
#     if status:
#         print(status, file=sys.stderr)
#     q.put(bytes(indata))
#
#
# def va_listen(callback):
#     with sd.RawInputStream(samplerate=Neko_setup.samplerate, blocksize=8000, device=Neko_setup.device, dtype='int16',
#                            channels=1, callback=q_callback):
#         rec = vosk.KaldiRecognizer(Neko_setup.model, Neko_setup.samplerate)
#         while True:
#             data = q.get()
#             if rec.AcceptWaveform(data):
#                 callback(json.loads(rec.Result())["text"])
#
class Voice_setup():
    def __init__(self):
        self.config_name = sqlite_Neko.read_config("config.yaml")
        if self.config_name["language"] == "ru":
            self.model = vosk.Model("model_ru")
        else:
            self.model = vosk.Model("model_en")
        self.samplerate = 16000
        self.device = self.config_name["device"]
        self.name_character = self.config_name["name_character"]
        self.commands = {}
        self.conn = sqlite_Neko.create_connection("Neko.db")
        self.stroke_console = ""

    def append_command_to_default(self):
        command_list = sqlite_Neko.voice_commands_source(self.conn)
        list_key = []
        for i in command_list:
            list_key.append(i[1])
        dst = dict.fromkeys(list_key, [])
        for i in command_list:
            dst[i[1]] = dst.get(i[1]) + [i[0]]
        self.commands.update(dst)
        print(self.commands)

class MyThread(threading.Thread):

    # Thread class with a _stop() method.
    # The thread itself has to check
    # regularly for the stopped() condition.

    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run
        threading.Thread.start(self)

    def __run(self):
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        if event == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, event, arg):
        if self.killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True

class TestVoice(QtWidgets.QDialog):
    def __init__(self):
        super(TestVoice, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setGeometry(QtCore.QRect(0, 0, 500, 800))
        self.setStyleSheet("background: rgba(23, 23, 23, 0.95);\n"
                           "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                           "border-radius: 13px;")
        self.label_q = QtWidgets.QLabel(self)
        self.label_q.setGeometry(QtCore.QRect(0, 0, 500, 700))
        self.label_q.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                   "font-family: \'Roboto Mono\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 14px;\n"
                                   "line-height: 18px;\n"

                                   "\n"
                                   "color: #FFFFFF;")
        self.label_q.setObjectName("label_q")
        self.label_q.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_q.setText("             ------------- - - -- - Testing your voice  - - - - -----------------\n"
                             "             ------------- - - -- -    Say anything   - - - - -----------------")
        self.button_back = QtWidgets.QPushButton(self)
        self.button_back.setGeometry(QtCore.QRect(250 - 81, 720, 81, 23))
        self.button_back.setStyleSheet("QPushButton {\n"
                                       "font-family: \'Roboto Mono\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 400;\n"
                                       "font-size: 18px;\n"
                                       "line-height: 18px;\n"
                                       "color: rgba(255, 255, 255, 0.8);background: rgba(23, 23, 23, 0.0);}\n"
                                       "QPushButton:hover{\n"
                                       "color: rgba(255, 255, 255, 1.0)\n"
                                       "}")
        self.button_back.setText("-- exit --")
        self.button_back.clicked.connect(self.close_app)
        self.Neko_setup = Voice_setup()
        self.Neko_setup.append_command_to_default()
        self.q = queue.Queue()
        self.Ne_flag = True
        self.hand = MyThread(target=self.reee)
        self.hand.start()

    @staticmethod
    def active_command_button_console(button_name):
        """считывает название кнопки, выполняет команду"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            sql_command_name = sqlite_Neko.select_all_command(conn)
            sql_command_type = sqlite_Neko.select_type_of_commands(conn)
            sql_command_files = sqlite_Neko.select_files_of_commands(conn)
            sql_command_site = sqlite_Neko.select_sites_of_command(conn)
            index = sql_command_name.index(button_name)
            command_type = sql_command_type[index]
            if command_type == 's':
                webbrowser.open_new_tab(str(sql_command_site[index]))
            elif command_type == 'f':
                for i in sql_command_files[index]:
                    print(sql_command_files[index])
                    if os.path.exists(i) is True:
                        subprocess.call(('cmd', '/c', 'start', '', i))
                    elif os.path.exists(i) is False:
                        pass

    def close_app(self):
        self.Ne_flag = False
        self.hand.kill()
        self.deleteLater()

    def q_callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def reee(self):
        print(1)
        self.va_listen_console(self.va_respond_console)

    def va_listen_console(self, callback):
        with sd.RawInputStream(samplerate=self.Neko_setup.samplerate, blocksize=8000, device=self.Neko_setup.device,
                            dtype='int16',
                            channels=1, callback=self.q_callback):

            rec = vosk.KaldiRecognizer(self.Neko_setup.model, self.Neko_setup.samplerate)
            while self.Ne_flag:
                try:
                    data = self.q.get()
                    if rec.AcceptWaveform(data):
                        callback(json.loads(rec.Result())["text"])
                except:
                    pass

    def va_respond_console(self, voice: str):
        if len(self.Neko_setup.stroke_console) > 500:
            self.Neko_setup.stroke_console = ""
        print("[Text]: ", voice)
        self.Neko_setup.stroke_console += f"[Text]:  {voice}\n"
        self.label_q.setText(self.Neko_setup.stroke_console)
        if self.Neko_setup.name_character != "":
            voice_input = voice.split(" ", 1)
            if len(voice_input) > 1:
                if fuzz.ratio(voice_input[0], self.Neko_setup.name_character) >= 20:
                    count = 0
                    for key in self.Neko_setup.commands:
                        for item in self.Neko_setup.commands[key]:
                            if fuzz.ratio(voice_input[1], item) >= 80:
                                self.active_command_button_console(key)
                                count += 1

                    if count == 0:
                        self.Neko_setup.stroke_console += f"Command not found\n"
                        self.label_q.setText(self.Neko_setup.stroke_console)
                else:
                    self.Neko_setup.stroke_console += f"--[Overlap]--: Get Name Character: {voice_input[0]} //  Expexting:{self.Neko_setup.name_character}\n"
                    self.label_q.setText(self.Neko_setup.stroke_console)
            else:
                self.Neko_setup.stroke_console += f"The first word must be the name of the character, followed by the \nname of command\n"
                self.label_q.setText(self.Neko_setup.stroke_console)

        else:
            self.Neko_setup.stroke_console += f"Character name is empty, the command is executed immediately\n"
            self.label_q.setText(self.Neko_setup.stroke_console)
            count = 0
            for key in self.Neko_setup.commands:
                for item in self.Neko_setup.commands[key]:
                    if fuzz.ratio(voice, item) >= 70:
                        self.active_command_button_console(key)
                        count += 1

            if count == 0:
                self.Neko_setup.stroke_console += f"Command not found\n"
                self.label_q.setText(self.Neko_setup.stroke_console)

class NekoVoice():
    def __init__(self):
        self.Neko_setup = Voice_setup()
        self.Neko_setup.append_command_to_default()
        self.q = queue.Queue()
        self.hand = MyThread(target=self.reee)
        self.hand.start()
        self.flag = True
        self.Ne_flag = True

    @staticmethod
    def active_command_button_console(button_name):
        """считывает название кнопки, выполняет команду"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            sql_command_name = sqlite_Neko.select_all_command(conn)
            sql_command_type = sqlite_Neko.select_type_of_commands(conn)
            sql_command_files = sqlite_Neko.select_files_of_commands(conn)
            sql_command_site = sqlite_Neko.select_sites_of_command(conn)
            index = sql_command_name.index(button_name)
            command_type = sql_command_type[index]
            if command_type == 's':
                webbrowser.open_new_tab(str(sql_command_site[index]))
            elif command_type == 'f':
                for i in sql_command_files[index]:
                    print(sql_command_files[index])
                    if os.path.exists(i) is True:
                        subprocess.call(('cmd', '/c', 'start', '', i))
                    elif os.path.exists(i) is False:
                        pass

    def manage(self):
        try:
            self.flag = not self.flag
            if self.flag:
                self.Ne_flag = True
                self.hand = MyThread(target=self.reee)
                self.hand.start()
            else:
                self.Ne_flag = False
                self.hand.kill()
                self.hand = None
        except:
            pass

    def update_setup(self):
        self.Neko_setup = Voice_setup()
        self.Neko_setup.append_command_to_default()

    def q_callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def reee(self):
        self.va_listen_console(self.va_respond_console)

    def va_listen_console(self, callback):
        with sd.RawInputStream(samplerate=self.Neko_setup.samplerate, blocksize=8000, device=self.Neko_setup.device,
                            dtype='int16',
                            channels=1, callback=self.q_callback):

            rec = vosk.KaldiRecognizer(self.Neko_setup.model, self.Neko_setup.samplerate)
            while self.Ne_flag:
                try:
                    data = self.q.get()
                    if rec.AcceptWaveform(data):
                        callback(json.loads(rec.Result())["text"])
                except:
                    pass

    def va_respond_console(self, voice: str):
        if len(self.Neko_setup.stroke_console) > 500:
            self.Neko_setup.stroke_console = ""
        print("[Text]: ", voice)
        if self.Neko_setup.name_character != "":
            voice_input = voice.split(" ", 1)
            if len(voice_input) > 1:
                if fuzz.ratio(voice_input[0], self.Neko_setup.name_character) >= 20:
                    for key in self.Neko_setup.commands:
                        for item in self.Neko_setup.commands[key]:
                            if fuzz.ratio(voice_input[1], item) >= 80:
                                self.active_command_button_console(key)
        else:
            for key in self.Neko_setup.commands:
                for item in self.Neko_setup.commands[key]:
                    if fuzz.ratio(voice, item) >= 70:
                        self.active_command_button_console(key)





if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # w = ErrorDialog()
    # w.exec_()
    # app.exec_()
    # va_listen(va_respond)
    # a = Neko_voice()
    pass
