#!/usr/bin/python
#-*- coding: utf-8 -*-
# Author: Ghost of Night

import re

colors = {
        'nc' : '\033[0m', #по умолчанию
        'bold' : '\033[1m', #усиленный (жирный или более интенсивный цвет)
        'low' : '\033[2m', #ослабленный (нежирный или менее интенсивный цвет)
        'underlined' : '\033[4m', #подчёркнутый
        'negative' : '\033[7m', #негативные цвета
        'hide' : '\033[8m', #скрытый
        'error' : '\033[9m', #перечёркнутый
        'black' : '\033[30m', #черный
        'red' : '\033[31m', #красный
        'green' : '\033[32m', #зелёный
        'yellow' : '\033[33m', #желтый
        'blue' : '\033[34m', #синий
        'magenta' : '\033[35m', #пурпурный
        'cyan' : '\033[36m', #голубой
        'white' : '\033[37m', #белый (светло-серый)
        'lblack' : '\033[90m', #ярко-черный
        'lred' : '\033[91m', #ярко-красный
        'lgreen' : '\033[92m', #ярко-зелёный
        'lyellow' : '\033[93m', #ярко-желтый
        'lblue' : '\033[94m', #ярко-синий
        'lmagenta' : '\033[95m', #ярко-пурпурный
        'lcyan' : '\033[96m', #ярко-голубой
	'lwhite' : '\033[97m', #ярко-белый
}

def cprint(txt, gettxt=False):
        txt = '%s{nc}' %(txt)
        colorList = re.findall('{([a-z]+)}', txt)
        for color in colorList:
                txt = txt.replace('{%s}' %(color), colors[color])
	if gettxt == False: print(txt)