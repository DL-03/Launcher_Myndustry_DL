import time
import PySimpleGUI as sg
from bs4 import BeautifulSoup
import requests
from urllib import request
import sys
import os
import os.path





comps = []

name  = 'download-Launcher_myndustry-DL.py'

loader = open('load.txt', 'r').readline()

toot = ''

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
# Load[:(len(name)*-1)] + 

font = 'fontello'

if os.path.exists(r'C:\Windows\Fonts\fontello.ttf') == False:
    os.system(f'{font}.ttf')

layout=[[sg.Button('Reload', key = '-update-', font=font), sg.Text("Alpha: 0.02, By: DL", font=font)],
[#sg.Frame(layout=[[sg.Button('1', key = '1b')],
# [sg.Button('2', key = '2b')],
# [sg.Button('3', key = '3b')],
# [sg.Button('4', key = '4b')],
# [sg.Button('5', key = '5b')],
# [sg.Button('6', key = '6b')],
# [sg.Button('7', key = '7b')],
# [sg.Button('8', key = '8b')],
# [sg.Button('9', key = '9b')],
# [sg.Button('10', key = '10b')]
# ], title='Github',title_color='white', relief=sg.RELIEF_SUNKEN), 
sg.Frame(layout=[
[sg.Listbox(['none'], font=font, key = 'list', size = (18, 25))],
[sg.Button('Open', key = 'go', font=font), sg.Button('More', key = 'more', font=font), sg.Button("Save", key = 'save', font=font)]
], title='Лаунчер',title_color='black', relief=sg.RELIEF_SUNKEN, font=font)]
        ]




window = sg.Window('Myndustry', layout)



print('Готово!')

def look():
    lister = []
    list_dir = os.listdir()
    try:
        r = requests.get('https://github.com/Anuken/MindustryBuilds/releases')
        html = BeautifulSoup(r.content, 'html.parser')
        items = html.findAll('div', class_ = 'release-entry')

        list_dir = os.listdir()
        x = 0
        for item in items:
            x += 1
            if x == 11:
                break
            try:    
                rt = item.find('div', class_ = 'f1 flex-auto min-width-0 text-normal').get_text(strip = True)
                comps.append(rt)
                if lister.count(rt) == list_dir.count(rt + '.jar'):
                    lister.append(rt + ' - Download')
                else:
                    lister.append(rt + ' - Open')
            except AttributeError:
                pass
            except IndexError:
                pass
            if page != 1:
                for o in range(0, page):
                    r = requests.get('https://github.com/Anuken/MindustryBuilds/releases' + f'?after={comps[-1]}')
                    html = BeautifulSoup(r.content, 'html.parser')
                    items = html.findAll('div', class_ = 'release-entry')

                    list_dir = os.listdir()
                    x = 0
                    for item in items:
                        x += 1
                        if x == 11:
                            break
                        try:    
                            rt = item.find('div', class_ = 'f1 flex-auto min-width-0 text-normal').get_text(strip = True)
                            comps.append(rt)
                            if lister.count(rt) == list_dir.count(rt + '.jar'):
                                lister.append(rt + ' - Download')
                            else:
                                lister.append(rt + ' - Open')
                        except AttributeError:
                            pass
                        except IndexError:
                            pass
        window['list'].update(lister)
        pass
    except Exception:
        try:
            window['list'].update(list_dir)
        except Exception:
            pass
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
def fr(sd):
    # second = values["list"]
    # sec = second[0]
    

    os.startfile(f'{save}{sd}.jar')
page = 1
event, values = window.read()  
look()
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

        page = 0
        # comps = []
        look()
        # window["1b"].update(comps[0])

    if event == 'go':
        cer = values["list"]
        cer = cer[0]
        cers = cer[8:]
        cerss = cer[8:]
        cerr = cer[:5]
        if values["list"] != '' or values["list"] != 'none':
            if cers == 'Open':
                print('ok')
            
                fr(cerr)
            if cers == 'Download':
                download(cerr)
            else:
                fr(cer)


    if event == 'save':
        sg.Popup('Для изменение путя сохранение файлов, в файле Save.txt измените путь')

    if event == 'more':
        page += 1
        look()

window.close()