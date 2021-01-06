import time
import PySimpleGUI as sg
from bs4 import BeautifulSoup
import requests
from urllib import request
import sys
import os
import os.path


layout=[[sg.Button('Reload', key = '-update-'), sg.Text("Alpha: 0.01, By: DL")],
[sg.Frame(layout=[[sg.Button('1', key = '1b')],
[sg.Button('2', key = '2b')],
[sg.Button('3', key = '3b')],
[sg.Button('4', key = '4b')],
[sg.Button('5', key = '5b')],
[sg.Button('6', key = '6b')],
[sg.Button('7', key = '7b')],
[sg.Button('8', key = '8b')],
[sg.Button('9', key = '9b')],
[sg.Button('10', key = '10b')]
], title='Github',title_color='white', relief=sg.RELIEF_SUNKEN), sg.Frame(layout=[
[sg.Listbox(['none'], key = 'list', size = (14, 16))],
[sg.Button('Luanch', key = 'go'), sg.Button("Save", key = 'save')]
], title='Computer',title_color='white', relief=sg.RELIEF_SUNKEN)]
        ]




window = sg.Window('Myndustry', layout)

buttons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



comps = []

name  = 'download-Launcher_myndustry-DL.py'

loader = open('load.txt', 'r').readline()


if os.path.exists(loader) == False:
    print('Подождите: Поиск файла установки...')
    for root, dirs, files in os.walk('C:\\'):
        if name in dirs or name in files:
            Load = f'{root}\{name}'
            ls = open('load.txt', 'w')
            ls.write(f'{root}\{name}')
            ls.close()
            break
    
else:
    Load = loader

print('Готово!')
r = requests.get('https://github.com/Anuken/MindustryBuilds/releases')
def look():
    
    html = BeautifulSoup(r.content, 'html.parser')
    items = html.findAll('div', class_ = 'release-entry')

    list_dir = os.listdir()
    window['list'].update(list_dir)
    x = 0
    for item in items:
        x += 1
        if x == 11:
            break
        try:
            
            comps.append(item.find('div', class_ = 'f1 flex-auto min-width-0 text-normal').get_text(strip = True)) # f1 flex-auto min-width-0 text-normal
            window[f"{x}b"].update(comps[x-1])
        except AttributeError:
            # comps.append(item.find('div', class_ = 'f1 flex-auto min-width-0 text-normal').get_text(strip = True))
            # window[f"{x}b"].update(item.find('svg', class_ = 'octicon octicon-tag d-md-none text-gray mr-1')) # item.find('svg', class_ = 'octicon octicon-tag d-md-none text-gray mr-1')
            pass
        except IndexError:
            pass
    # for x in range(1, len(comps)+1):
    #     window[f"{x}b"].update(comps[x-1])
sak = ''
def download(y):
    s = open(r'DON.txt', 'w') # C:\Users\DL\Desktop\calculator DL 1.0\
    s.write(y)
    window.hide
    s.close
    os.startfile(Load) # C:\Users\DL\Desktop\calculator DL 1.0\
    # sak = y
    # sg.one_line_progress_meter('Downloading', 0, 2, 'key','Wait...')
    # request.urlretrieve(f'https://github.com/Anuken/MindustryBuilds/releases/download/{y}/Mindustry-BE-Desktop-{y}.jar', f'{save}{y}.jar')
    # sg.one_line_progress_meter('Downloading', 1, 2, 'key','Wait...')
    # look()
    # time.sleep(1)
    # sg.one_line_progress_meter('Downloading', 2, 2, 'key','Wait...')
save = open( r'Save.txt', 'r' ).readline()
os.chdir(save)
def fr():
    second = values["list"]
    sec = second[0]


    os.startfile(f'{save}{sec}')

event, values = window.read()  
list_dir = os.listdir()
look()
window['list'].update(list_dir)
while True:
    list_dir = os.listdir()

    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    y = 0

    for x in range(1, 11):
        if event == f'{x}b':
            download(comps[x - 1])
            window['list'].update(list_dir)

    
    
    if event == '-update-':

        
        # comps = []
        look()
        # window["1b"].update(comps[0])

    if event == 'go':

        if list_dir != '' or list_dir != 'none':
            fr()

    if event == 'save':
        sg.Popup('Для изменение путя сохранение файлов, в файле Save.txt измените путь')


window.close()