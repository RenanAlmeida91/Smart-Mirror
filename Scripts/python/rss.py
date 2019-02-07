#BUSCA RSS
#==================
#importa bibliotecas:
import urllib
import xml.etree.ElementTree as ET
from random import randint

#define a URL e parametros
UOL_HOME_URL = "http://rss.home.uol.com.br/index.xml"
UOL_NOTICIAS_URL = "http://rss.uol.com.br/feed/noticias.xml"
UOL_ECONOMIA_URL = "http://rss.uol.com.br/feed/economia.xml"
UOL_JOGOS_URL = "http://rss.jogos.uol.com.br/ultnot/index.xml"
G1_HOME_URL = "http://g1.globo.com/dynamo/rss2.xml"
G1_AUTOESPORTE_URL = "http://g1.globo.com/dynamo/carros/rss2.xml"
G1_CES_URL = "http://g1.globo.com/dynamo/ciencia-e-saude/rss2.xml"
G1_ECONOMIA_URL = "http://g1.globo.com/dynamo/economia/rss2.xml"
G1_MUNDO_URL = "http://g1.globo.com/dynamo/mundo/rss2.xml"
G1_BRASIL_URL = "http://g1.globo.com/dynamo/brasil/rss2.xml"
G1_MUSICA_URL = "http://g1.globo.com/dynamo/musica/rss2.xml"
G1_POLITICA_URL = "http://g1.globo.com/dynamo/politica/mensalao/rss2.xml"
G1_POP_URL = "http://g1.globo.com/dynamo/pop-arte/rss2.xml"
G1_TECNOLOGIA_URL = "http://g1.globo.com/dynamo/tecnologia/rss2.xml"
TERRA_BRASIL_URL = "http://rss.terra.com.br/0,,EI1,00.xml"

#busca na web e retorna uma noticia aleatoria dentre as escolhidas
def buscarss(str):
	if (str == "0000000000000000"):
		return ("Zero!")
	i = randint(1,21)
	i=7
	if (i == 1) and (str[0] == "1"):
	# busca UOL HOME
		url = urllib.urlopen(UOL_HOME_URL).read()
		tree = ET.fromstring(url)
		j = randint(8,20)
		for item in tree.findall('channel'):
			return('UOL: '+item[j][0].text.encode('UTF-8'))
	elif (i == 2) and (str[1] == "1"):
	#busca UOL NOTICIAS
		url = urllib.urlopen(UOL_NOTICIAS_URL).read()
		j = randint(8,15)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			return('UOL: '+item[j][0].text.strip().encode('UTF-8'))
	elif (i == 3) and (str[2] == "1"):
	#busca UOL ECONOMIA
		url = urllib.urlopen(UOL_ECONOMIA_URL).read()
		j = randint(8,15)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			return('UOL: '+item[j][0].text.strip().encode('UTF-8'))
	elif (i == 4) and (str[3] == "1"):
	#busca UOL JOGOS
		url = urllib.urlopen(UOL_JOGOS_URL).read()
		j = randint(8,15)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			return('UOL: '+item[j][0].text.strip().encode('UTF-8'))
	elif (i == 5) and (str[4] == "1"):
	#busca G1 HOME
		url = urllib.urlopen(G1_HOME_URL).read()
		j = randint(8,40)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			print(repr(item[j][0].text.strip().encode('UTF-8')))
			return('G1: '+item[j][0].text.strip().encode('UTF-8'))	
	elif (i == 6) and (str[5] == "1"):
	#busca G1 AUTOESPORTE
		url = urllib.urlopen(G1_AUTOESPORTE_URL).read()
		j = randint(8,20)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			return('G1: '+item[j][0].text.strip().encode('UTF-8'))
	elif (i == 7) and (str[6] == "1"):
	#busca G1 CIENCIA E SAUDE
		url = urllib.urlopen(G1_CES_URL).read()
		j = randint(8,20)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			return('G1: '+item[j][0].text.strip().encode('UTF-8'))
	elif (i == 8) and (str[7] == "1"):
	#busca G1 ECONOMIA
		url = urllib.urlopen(G1_ECONOMIA_URL).read()
		j = randint(8,20)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			return('G1: '+item[j][0].text.strip().encode('UTF-8'))
	elif (i == 9) and (str[8] == "1"):
	#busca G1 MUNDO
		url = urllib.urlopen(G1_MUNDO_URL).read()
		j = randint(8,20)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			return('G1: '+item[j][0].text.strip().encode('UTF-8'))
	elif (i == 10) and (str[9] == "1"):
	#busca G1 BRASIL
		url = urllib.urlopen(G1_BRASIL_URL).read()
		j = randint(8,20)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			return('G1: '+item[j][0].text.strip().encode('UTF-8'))
	elif (i == 11) and (str[10] == "1"):
	#busca G1 MUSICA
		url = urllib.urlopen(G1_MUSICA_URL).read()
		j = randint(8,20)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			return('G1: '+item[j][0].text.strip().encode('UTF-8'))
	elif (i == 12) and (str[11] == "1"):
	#busca G1 MUSICA
		url = urllib.urlopen(G1_MUSICA_URL).read()
		j = randint(8,20)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			return('G1: '+item[j][0].text.strip().encode('UTF-8'))
	elif (i == 13) and (str[12] == "1"):
	#busca G1 POLITICA
		url = urllib.urlopen(G1_POLITICA_URL).read()
		j = randint(8,20)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			return('G1: '+item[j][0].text.strip().encode('UTF-8'))
	elif (i == 14) and (str[13] == "1"):
	#busca G1 POP
		url = urllib.urlopen(G1_POP_URL).read()
		j = randint(8,20)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			return('G1: '+item[j][0].text.strip().encode('UTF-8'))
	elif (i == 15) and (str[14] == "1"):
	#busca G1 TECNOLOGIA
		url = urllib.urlopen(G1_TECNOLOGIA_URL).read()
		j = randint(8,20)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			return('G1: '+item[j][0].text.strip().encode('UTF-8'))
	elif (i == 16) and (str[15] == "1"):
	#busca TERRA BRASIL
		url = urllib.urlopen(TERRA_BRASIL_URL).read()
		j = randint(5,14)
		tree = ET.fromstring(url)
		for item in tree.findall('channel'):
			return('TERRA: '+item[j][0].text.strip().encode('UTF-8'))

#print(buscarss("11111"))