import time
import PySimpleGUI as sg
from bs4 import BeautifulSoup
import requests
from urllib import request
import sys
import os

y = open( r'DON.txt', 'r' ).readline()

save = open( r'Save.txt', 'r' ).readline()


sg.one_line_progress_meter(f'Downloading {y}', 0, 2, 'key','Подождите, скачивание файлов из интернета будут проводица в зависнутом окне(не отвечает!)')
request.urlretrieve(f'https://github.com/Anuken/MindustryBuilds/releases/download/{y}/Mindustry-BE-Desktop-{y}.jar', f'{save}{y}.jar')
sg.one_line_progress_meter(f'Downloading {y}', 1, 2, 'key','Готово!')
time.sleep(1)
sg.one_line_progress_meter(f'Downloading {y}', 2, 2, 'key','Готово!')