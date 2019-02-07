#MOSTRA HORA
#VER https://www.daniweb.com/programming/software-development/code/216785/tkinter-digital-clock-python
#==================
#importa bibliotecas:
import time
import datetime

#retorna hora ou data
def tempo(param):
	if param == 1:
		hora = time.strftime('%H:%M:%S')
		return hora
	elif param == 2:
		data = time.strftime("%d/%m/%Y")
		return data
	else:
		print("ERRO")