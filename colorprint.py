"""
Print colored text to the console
  cprint('{lred}%s {nc}=> {lyellow}%s {nc}: {lgreen}%s' %('Server', 'Service Name', 'Port'))
Supported colors:
yellow, lblue, cyan, magenta, blue, hide, nc, negative,
black, low, white, red, lgreen, bold, lmagenta,
underlined, lcyan, lblack, lyellow, lwhite, green, lred, error
"""

#!/usr/bin/python
#-*- coding: utf-8 -*-
# Author: Ghost of Night

import re

__all__ = ["cprint"]

colors = {
	'nc' : '\033[0m', #po umolchaniyu
	'bold' : '\033[1m', #usilennyj (zhirnyj ili bolee intensivnyj cvet)
	'low' : '\033[2m', #oslablennyj (nezhirnyj ili menee intensivnyj cvet)
	'underlined' : '\033[4m', #podchyorknutyj
	'negative' : '\033[7m', #negativnye cveta
	'hide' : '\033[8m', #skrytyj
	'error' : '\033[9m', #perechyorknutyj
	'black' : '\033[30m', #chernyj
	'red' : '\033[31m', #krasnyj
	'green' : '\033[32m', #zelyonyj
	'yellow' : '\033[33m', #zheltyj
	'blue' : '\033[34m', #sinij
	'magenta' : '\033[35m', #purpurnyj
	'cyan' : '\033[36m', #goluboj
	'white' : '\033[37m', #belyj (svetlo-seryj)
	'lblack' : '\033[90m', #yarko-chernyj
	'lred' : '\033[91m', #yarko-krasnyj
	'lgreen' : '\033[92m', #yarko-zelyonyj
	'lyellow' : '\033[93m', #yarko-zheltyj
	'lblue' : '\033[94m', #yarko-sinij
	'lmagenta' : '\033[95m', #yarko-purpurnyj
	'lcyan' : '\033[96m', #yarko-goluboj
	'lwhite' : '\033[97m', #yarko-belyj
}

def cprint(txt, gettxt=False):
	txt = '%s{nc}' %(txt)
	colorList = re.findall('{([a-z]+)}', txt)
	for color in colorList:
		txt = txt.replace('{%s}' %(color), colors[color])
	if gettxt == False: print(txt)
