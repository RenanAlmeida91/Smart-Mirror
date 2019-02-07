from currency import *
from rss import *
from weather import *
from hour import *
from comm import *
import curses
import time
import dateutil.parser
#import logging
#logging.basicConfig(filename='example.log',level=logging.DEBUG)
#logging.info('I told you so')


"""eventos = calendar_eventos(2, 'anderson', credentials)
for event in eventos:
	start = event['start'].get('dateTime')
	print(dateutil.parser.parse(start.encode('UTF-8')).strftime("%X - %x")+" - "+event['summary'].encode('UTF-8'))
	
while True:
	print ("lol")
	time.sleep(100)
"""

def verificalogin():
	return 2

DBHOST = "localhost"
DBUSER = "root"
DBPW = "toor"
DBASE  = "MIRROR_EDGE"
DBTABLE = "USERS"
		
#CRIA DB SE NAO EXISTE
try:
	criadbsql(DBHOST,DBUSER,DBPW,DBASE)
	criatbsql(DBHOST,DBUSER,DBPW,DBASE,"USERS")
except:
	pass

credentials = get_credentials(verificalogin())
#START DA APLICACAO
myscreen = curses.initscr()
curses.curs_set(0)
curses.cbreak()
while True:
	while verificaconfig() == True:
			#VERIFICA SE JA EXISTE ALGUMA CONFIGURACAO
			#SE NAO, INICIA CONFIGURACAO
			print("INICIANDO CONFIGURACAO...")
			CONFIG_BRUTO = decriptomens(tcprcv()[0],CHAVE)
			CONFIG =  CONFIG_BRUTO.split('|')
			escdatasql(DBHOST,DBUSER,DBPW,DBASE,DBTABLE,"'"+CONFIG[0]+"'","'"+CONFIG[1]+"'","'"+CONFIG[2]+"'","'"+CONFIG[3]+"'","'"+CONFIG[4]+"'","'"+CONFIG[5]+"'","'"+CONFIG[6]+"'","'"+CONFIG[7]+"'","'"+CONFIG[8]+"'","'"+CONFIG[9]+"'","'"+CONFIG[10]+"'")
			os.system("rm -rf ~/TCC/config.txt")
			#CONCLUIDO
		#INICIA NORMALMENTE
	while True:
		#VERIFICA SE E NECESSARIO CONFIGURAR DE NOVO
		if verificaconfig() == True:
			break
		else:
			#VERIFICA SE HA ALGUEM NA FRENTE
			while verificalogin() != 0:
				USER = verificalogin()
				#LE AS CONFIGS
				try:
					USER_CONFIG = ledatasql(DBHOST,DBUSER,DBPW,DBASE,DBTABLE,'*',"'"+str(USER)+"'")
					MOEDA1=buscamoeda(USER_CONFIG[0][6])
					MOEDA2=buscamoeda(USER_CONFIG[0][7])
					TEMP1=buscaclima(str(USER_CONFIG[0][4]),1)
					TEMP2=buscaclima(str(USER_CONFIG[0][5]),1)
					RSS=buscarss(USER_CONFIG[0][8])
					while ( RSS == "Zero!" ):
						RSS=buscarss(USER_CONFIG[0][8])
					eventos = calendar_eventos(1, USER, credentials)	
					for event in eventos:
						start = event['start'].get('dateTime')
						prox_evento = dateutil.parser.parse(start.encode('UTF-8')).strftime("%X - %x")+" - "+event['summary'].encode('UTF-8')
				except:
					pass
				if verificaconfig() == True:
						myscreen.clear()
						win_relogio.refresh()
						win_relogio.clear()
						win_nome.refresh()
						win_nome.clear()
						win_moeda.refresh()
						win_moeda.clear()
						win_temp.refresh()
						win_temp.clear()
						win_rss.refresh()
						win_rss.clear()
						win_cal.refresh()
						win_cal.clear()
						break
				#PASSA AS CONFIGS PARA OS METODOS DE BUSCA
				for i in range(0, 100000):
					myscreen.clear()
					#newwin(height, width, begin_y, begin_x)
					win_relogio = curses.newwin(3, 10, 0, 0)
					win_relogio.border("|","|","-","-","+","+","+","+")
					win_relogio.addstr(1,1,tempo(1))
					win_nome = curses.newwin(3, 90, 0, 11)
					win_nome.border("|","|","-","-","+","+","+","+")
					win_nome.addstr(1,1,"              "+USER_CONFIG[0][1]+" "+USER_CONFIG[0][2]+" || "+USER_CONFIG[0][3])
					win_moeda = curses.newwin(3, 35, 3, 0)
					win_moeda.border("|","|","-","-","+","+","+","+")
					win_moeda.addstr(1,1,"  "+USER_CONFIG[0][6]+" "+MOEDA1+" || "+USER_CONFIG[0][7]+": "+MOEDA2)
					win_temp = curses.newwin(3, 65, 3, 36)
					win_temp.border("|","|","-","-","+","+","+","+")
					win_temp.addstr(1,1,"                       SP: "+TEMP1+" || NY: "+TEMP2)#+unichr(176)+'C'
					win_rss = curses.newwin(5, 101, 6, 0)
					win_rss.border("|","|","-","-","+","+","+","+")
					win_rss.addstr(1,1,RSS)
					win_cal = curses.newwin(5, 101, 11, 0)
					win_cal.border("|","|","-","-","+","+","+","+")
					win_cal.addstr(1,1,prox_evento)
					win_relogio.refresh()
					win_relogio.clear()
					win_nome.refresh()
					win_nome.clear()
					win_moeda.refresh()
					win_moeda.clear()
					win_temp.refresh()
					win_temp.clear()
					win_rss.refresh()
					win_rss.clear()
					win_cal.refresh()
					win_cal.clear()
			#SE NAO, USA CONFIGURACAO PADRAO:
			try:
				PADRAO = ledatasql(DBHOST,DBUSER,DBPW,DBASE,DBTABLE,'*','1')
				DOLAR=buscamoeda(PADRAO[0][6])
				EURO=buscamoeda(PADRAO[0][7])
				TEMP1=buscaclima(str(PADRAO[0][4]),1)
				TEMP2=buscaclima(str(PADRAO[0][5]),1)
				RSS=buscarss(PADRAO[0][8])
			except:
				pass
			for i in range(0, 100000):
				myscreen.clear()
				#newwin(height, width, begin_y, begin_x)
				win_relogio = curses.newwin(3, 10, 0, 0)
				win_relogio.border("|","|","-","-","+","+","+","+")
				win_relogio.addstr(1,1,tempo(1))
				win_nome = curses.newwin(3, 90, 0, 11)
				win_nome.border("|","|","-","-","+","+","+","+")
				win_nome.addstr(1,1,"              "+PADRAO[0][1]+" "+PADRAO[0][2]+" || "+PADRAO[0][3])
				win_moeda = curses.newwin(3, 35, 3, 0)
				win_moeda.border("|","|","-","-","+","+","+","+")
				win_moeda.addstr(1,1,"  DOLAR: "+DOLAR+" || EURO: "+EURO)
				win_temp = curses.newwin(3, 65, 3, 36)
				win_temp.border("|","|","-","-","+","+","+","+")
				win_temp.addstr(1,1,"                       SP: "+TEMP1+" || NY: "+TEMP2)#+unichr(176)+'C'
				win_rss = curses.newwin(5, 101, 6, 0)
				win_rss.border("|","|","-","-","+","+","+","+")
				win_rss.addstr(1,1,RSS)
				win_relogio.refresh()
				win_relogio.clear()
				win_nome.refresh()
				win_nome.clear()
				win_moeda.refresh()
				win_moeda.clear()
				win_temp.refresh()
				win_temp.clear()
				win_rss.refresh()
				win_rss.clear()
				if verificaconfig() == True:
					myscreen.clear()
					win_relogio.refresh()
					win_relogio.clear()
					win_nome.refresh()
					win_nome.clear()
					win_moeda.refresh()
					win_moeda.clear()
					win_temp.refresh()
					win_temp.clear()
					win_rss.refresh()
					win_rss.clear()
					break