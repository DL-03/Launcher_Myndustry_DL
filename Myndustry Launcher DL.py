from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QProgressBar, QGridLayout, QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from ui import *

import sys

import time
from bs4 import BeautifulSoup
import requests
from urllib import request
import sys
import os

if os.path.exists('C:\\Windows\\Fonts\\fontello.ttf') == False:
    os.system('fontello.ttf')

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
load = os.getcwd()

save = open( f'{load}\\save.txt', 'r' ).readline()

list_dir = os.listdir(save)

Form.setMinimumHeight(370)
Form.setMinimumWidth(270)

page = 1


def reloadd():
        page = 1
        listerr = []
        lister = []
        ui.listBE.clear()
        r = requests.get('https://github.com/Anuken/MindustryBuilds/releases')
        html = BeautifulSoup(r.content, 'html.parser')
        items = html.findAll('div', class_ = 'release-entry')  
        x = 0
        for item in items:
                x += 1
                if x == 11:
                    break
                try:    
                    rt = item.find('div', class_ = 'f1 flex-auto min-width-0 text-normal').get_text(strip = True)
                    listerr.append(rt)
                    if lister.count(rt) == list_dir.count(rt + '.jar'):
                        lister.append(rt + ' - Download')
                    else:
                        lister.append(rt + ' - Open')
                except Exception:
                    pass
        for i in range(0, len(lister)):
                ui.listBE.addItem(lister[i])
def moree():
        global page
        page = page + 1
        listerr = []
        lister = []
        ui.listBE.clear()
        r = requests.get('https://github.com/Anuken/MindustryBuilds/releases')
        html = BeautifulSoup(r.content, 'html.parser')
        items = html.findAll('div', class_ = 'release-entry')  
        x = 0
        for item in items:
                x += 1
                if x == 11:
                    break
                try:    
                    rt = item.find('div', class_ = 'f1 flex-auto min-width-0 text-normal').get_text(strip = True)
                    listerr.append(rt)
                    if lister.count(rt) == list_dir.count(rt + '.jar'):
                        lister.append(rt + ' - Download')
                    else:
                        lister.append(rt + ' - Open')
                except Exception:
                    pass
        if page != 1:
                for o in range(0, page):
                        r = requests.get('https://github.com/Anuken/MindustryBuilds/releases?after=' + listerr[-1])
                        html = BeautifulSoup(r.content, 'html.parser')
                        items = html.findAll('div', class_ = 'release-entry')  
                        x = 0
                        for item in items:
                                x += 1
                                if x == 11:
                                        break
                                try:    
                                        rt = item.find('div', class_ = 'f1 flex-auto min-width-0 text-normal').get_text(strip = True)
                                        listerr.append(rt)
                                        if lister.count(rt) == list_dir.count(rt + '.jar'):
                                                lister.append(rt + ' - Download')
                                        else:
                                                lister.append(rt + ' - Open')
                                except Exception:
                                        pass
        for i in range(0, len(lister)):
                ui.listBE.addItem(lister[i])


def error():
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка!")
        msg.setText('Ошибка при нажатие на кнопку "Open"')
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

def download(y):
        s = open(load + '\\num.txt', 'w') # C:\Users\DL\Desktop\calculator DL 1.0\
        s.write(y)
        s.close
        os.startfile(load + '\\download_main.py')





def opens():
        sd = ''
        for item in ui.listBE.selectedItems():
                sd = item.text()
        if sd != '':
                sk = ''
                ol = ''
                oll = ''
                skl = ''
                # sd = ui.listBE.selectedItems()
                try:
                        for item in ui.listBE.selectedItems():
                            sd = item.text()
                        for o in range(0, len(sd)):
                                if ol == ' ':
                                        break
                                ol = sd[o]
                                sk = sd[:o]
                        for l in range(0, len(sd)):
                                oll = sd[l*-1]
                                skl = sd[l*-1:]
                                if oll == ' ':
                                        break
                        
                        skl = skl[1:]
                        if skl == 'Open':
                                os.startfile(f'{save}{sk}.jar')
                        elif skl == 'Download':
                                download(sk)
                        else:
                                error()

                except Exception:
                        error()
        else:
                error()


def isave():
    msg = QMessageBox()
    msg.setWindowTitle("Информация сохронение!")
    msg.setText('Для изменение рабочей области файлов Myndustry - В папке с лаунчером в файле save.txt измените путь!')
    msg.setIcon(QMessageBox.Info)
    msg.setStandardButtons(QMessageBox.Ok)
    x = msg.exec_()

page = 1
ui.Reload.clicked.connect(reloadd)
ui.More.clicked.connect(moree)
ui.Open.clicked.connect(opens)
ui.Save.clicked.connect(isave)
# ui.window.resized.connect(resize)


sys.exit(app.exec_())