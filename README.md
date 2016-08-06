# colorprint
Color print function for Python

Usample usage:
```python
from colorprint import cprint

cprint('{lred}%s {nc}=> {lyellow}%s {nc}: {lgreen}%s' %('Server', 'Service Name', 'Port'))
```
![example_image](https://cloud.githubusercontent.com/assets/20622766/17458852/78a6cf04-5c32-11e6-9314-3dfc2e1202de.png)

##You can choose next colors
```pyton
'nc' : #по умолчанию
'bold' : #усиленный (жирный или более интенсивный цвет)
'low' : #ослабленный (нежирный или менее интенсивный цвет)
'underlined' : #подчёркнутый
'negative' : #негативные цвета
'hide' : #скрытый
'error' : #перечёркнутый
'black' : #черный
'red' : #красный
'green' : #зелёный
'yellow' : #желтый
'blue' : #синий
'magenta' : #пурпурный
'cyan' : #голубой
'white' : #белый (светло-серый)
'lblack' : #ярко-черный
'lred' : #ярко-красный
'lgreen' : #ярко-зелёный
'lyellow' : #ярко-желтый
'lblue' : #ярко-синий
'lmagenta' : #ярко-пурпурный
'lcyan' : #ярко-голубой
'lwhite' : #ярко-белый
```
