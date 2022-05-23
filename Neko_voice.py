import subprocess
import sys
import os.path
import sys
import webbrowser
import sqlite_Neko
import traceback
import random
import pyttsx3
import speech_recognition as sr
import webbrowser
import wave
import json
from vosk import Model, KaldiRecognizer
import wikipediaapi
import keyboard
from PyQt5.QtGui import QKeySequence, QWheelEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
from Neko_layout import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


def voice_helper():
	voice_input = record_and_recognize_audio()
	os.remove("microphone-results.wav")
	print(voice_input)
	voice_input = voice_input.split(" ")
	command = voice_input[0]
	command_options = [str(input_part) for input_part in voice_input[1:len(voice_input)]]
	execute_command_with_name(command, command_options)
