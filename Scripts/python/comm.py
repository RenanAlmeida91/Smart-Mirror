#INICIA E TRATA REQUISICOES DO APLICATIVO
#==================
#IMPORTA BIBLIOTECAS
#https://github.com/google/oauth2client/blob/master/oauth2client/tools.py
from __future__ import print_function
import socket
from Crypto.Cipher import AES
import time
import sys
import MySQLdb
import os.path
import httplib2
import os
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import datetime
import logging
import socket
import sys
from six.moves import BaseHTTPServer
from six.moves import http_client
from six.moves import urllib
from six.moves import input
from oauth2client import client
from oauth2client import util

#DEFINE VARIAVEIS
HOST = ''                 # TODAS AS INTERFACES
PORT = 55505              # PORTA ARBITRARIA PRIVADA BRDC
PORT2 = 55506              # PORTA2 ARBITRARIA PRIVADA UNC
CHAVE = 'FALCAO EH TROUXA' #CHAVE CRIPTOGRAFIA
SENHA = 'Q_Q_TA_CONTE_SENO'	#SENHA CRIPTOGRAFIA
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly https://www.googleapis.com/auth/gmail.readonly https://www.googleapis.com/auth/fitness.body.read' #GOOGLE API
CLIENT_SECRET_FILE = '/home/ubuntu/TCC/client_secret.json' #GOOGLE API
APPLICATION_NAME = 'Smart Mirror'	#GOOGLE API

#CRIA SOCKET E ESCUTA BROADCAST
def broadcastrcv():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((HOST, PORT))
	BROADC = s.recvfrom(1024)
	BROADC_DEC = decriptomens(BROADC[0],CHAVE)
	if BROADC_DEC == SENHA:
		SRCIP = BROADC[1][0]
	else:
		SRCIP = "UNKNOW"
	return SRCIP

#CRIA SOCKET E ESCUTA TCP
def tcprcv():
	g = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	g.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	g.settimeout(120.0)
	g.bind((HOST, PORT2))
	g.listen(1)
	conn, addr = g.accept()
	DADOS = conn.recv(1024)
	conn.close()
	return DADOS,addr

#CRIA SOCKET E ENVIA TCP
def tcpsnd(DADOS,IP,PORT):
	r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	r.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	r.settimeout(120.0)
	r.connect((IP, PORT))
	r.sendall(DADOS)
	r.close()

#CRIPTOGRAFA MENSAGEM
def criptomens(MENS,CHAVE):
	length = 16 - (len(MENS) % 16)
	MENS += chr(length)*length
	obj = AES.new(CHAVE, AES.MODE_CBC, 'This is an IV456')
	return obj.encrypt(MENS)

#DESCRIPTOGRAFA MENSAGEM
def decriptomens(MENS,CHAVE):
	obj = AES.new(CHAVE, AES.MODE_CBC, 'This is an IV456')
	str_a = obj.decrypt(MENS).split()[0].strip('\x0f').strip('\x08')
	return str_a

#RECEBE NOME
def recebenome():
	NOME = decriptomens(tcprcv()[0],CHAVE);
	return ("'"+NOME+"'")
	
#RECEBE SOBRENOME
def recebesobrenome():
	SOBRENOME = decriptomens(tcprcv()[0],CHAVE);
	return ("'"+SOBRENOME+"'")
	
#CRIA BANCO SQL
def criadbsql(HOST,USER,PW,BANCO):
	dbmirror = MySQLdb.connect (HOST, USER, PW)
	cursor = dbmirror.cursor()
	cursor.execute('CREATE DATABASE '+BANCO)
	dbmirror.commit()
	dbmirror.close()
	
#DELETA BANCO SQL
def deldbsql(HOST,USER,PW):
	dbmirror = MySQLdb.connect (HOST,USER,PW)
	cursor = dbmirror.cursor()
	cursor.execute('DROP DATABASE MIRROR_EDGE;')
	dbmirror.commit()
	dbmirror.close()

#CRIA TABELA SQL
def criatbsql(HOST,USER,PW,BANCO,TABELA):
	dbmirror = MySQLdb.connect (HOST, USER, PW, BANCO)
	cursor = dbmirror.cursor()
	cursor.execute('CREATE TABLE '+TABELA+' ('+' ID int AUTO_INCREMENT PRIMARY KEY, NOME varchar(255) NOT NULL, SOBRENOME varchar(255) NOT NULL, EMAIL varchar(255) NOT NULL UNIQUE, CIDADE1 int(20), CIDADE2 int(20), MOEDA1 varchar(3), MOEDA2 varchar(3), RSS varchar(255) NOT NULL, CONEXAO int(1) NOT NULL, SSID varchar(255), WLANPW varchar(255));')
	cursor.execute('INSERT INTO '+TABELA+" (NOME, SOBRENOME, EMAIL, CIDADE1, CIDADE2, MOEDA1, MOEDA2, RSS, CONEXAO, SSID, WLANPW) VALUES ('CONFIG','PADRAO','support@falcon.com.br','3448439','5128638','USD','EUR','1111111111111111','0','','');")
	dbmirror.commit()
	dbmirror.close()
	
#COLOCA DADOS NA TABELA SQL
def escdatasql(HOST,USER,PW,BANCO,TABELA,NOME,SOBRENOME,EMAIL,CIDADE1,CIDADE2,MOEDA1,MOEDA2,RSS,CONEXAO,SSID,WLANPW):
	dbmirror = MySQLdb.connect (HOST, USER, PW, BANCO)
	cursor = dbmirror.cursor()
	cursor.execute('INSERT INTO '+TABELA+' (NOME, SOBRENOME, EMAIL, CIDADE1, CIDADE2, MOEDA1, MOEDA2, RSS, CONEXAO, SSID, WLANPW) VALUES ('+NOME+','+SOBRENOME+','+EMAIL+','+CIDADE1+','+CIDADE2+','+MOEDA1+','+MOEDA2+','+RSS+','+CONEXAO+','+SSID+','+WLANPW+');')
	dbmirror.commit()
	dbmirror.close()
	
#COLOCA DADOS NA TABELA SQL
def ledatasql(HOST,USER,PW,BANCO,TABELA,DADO,PERSON):
	dbmirror = MySQLdb.connect (HOST, USER, PW, BANCO)
	cursor = dbmirror.cursor()
	cursor.execute('SELECT '+DADO+' FROM '+TABELA+' WHERE ID='+PERSON+';')
	dadolido = cursor.fetchall()
	dbmirror.commit()
	dbmirror.close()
	return dadolido
	
#VERIFICA SE E NECESSARIO CONFIGURAR
def verificaconfig():
	return os.path.isfile("/home/ubuntu/TCC/config.txt")

#RECEBE CREDENCIAIS GOOGLE
def get_credentials(user):
	home_dir = os.path.expanduser('~')
	credential_dir = os.path.join(home_dir, '.credentials')
	if not os.path.exists(credential_dir):
		os.makedirs(credential_dir)
	user_path = str(user)+".json"
	credential_path = os.path.join(credential_dir, user_path)
	store = oauth2client.file.Storage(credential_path)
	credentials = store.get()
	if not credentials or credentials.invalid:
		flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
		flow.user_agent = APPLICATION_NAME
		oauth_callback = client.OOB_CALLBACK_URN
		flow.redirect_uri = oauth_callback
		authorize_url = flow.step1_get_authorize_url()
		print('    ' + authorize_url)
		#MANDAR authorize_url PARA O APP E RECEBER O CODIGO
		code = input('Enter verification code: ').strip()
		try:
			credentials = flow.step2_exchange(code)
		except client.FlowExchangeError as e:
			sys.exit('Authentication has failed: %s' % e)
		store.put(credentials)
		credentials.set_store(store)
		print('Storing credentials to ' + credential_path)
	return credentials

def calendar_eventos(neventos, user, credentials):
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('calendar', 'v3', http=http)
	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	eventsResult = service.events().list(calendarId='primary', timeMin=now, maxResults=neventos, singleEvents=True, orderBy='startTime').execute()
	events = eventsResult.get('items', [])
	if not events:
		print('Nenhum evento')
		return ("Nenhum evento")
	return events
		
