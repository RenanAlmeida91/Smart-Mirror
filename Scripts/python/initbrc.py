import os
from comm import *

while True:
	IP = broadcastrcv()
	if IP != "UNKNOW":
		thismirror =  socket.gethostname()
		tcpsnd(criptomens(thismirror,CHAVE),IP,PORT2)
		try:
			CONFIGCLIENT = tcprcv()
			if decriptomens(CONFIGCLIENT[0],CHAVE) == "s":
				os.system("touch ~/TCC/config.txt")
				texto = open("config.txt", 'w')
				texto.write(IP)
				texto.close()
		except:
			pass