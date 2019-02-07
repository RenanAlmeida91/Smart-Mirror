#BUSCA CLIMA OPENWEATHER
#==================
#importa bibliotecas:
import urllib
import xml.etree.ElementTree as ET

#define a URL e parametros
owurlforecast = "http://api.openweathermap.org/data/2.5/forecast/daily?id="
owurlcurrent = "http://api.openweathermap.org/data/2.5/weather?id="
owformat = "xml"
owID = "4c3ddb738f9fbefdbb28963642aafc1a"
owunit = "metric"
lang = "pt"
cnt = "1"

#busca na web
def buscaclima(cidadeid,param):
	if param==1:
	#busca temperatura atual
		climabruto = urllib.urlopen(owurlcurrent+cidadeid+'&mode='+owformat+'&APPID='+owID+'&units='+owunit+'&cnt=1&lang='+lang).read()
	else:
		#busca temperatura prevista
		climabruto = urllib.urlopen(owurlforecast+cidadeid+'&mode='+owformat+'&APPID='+owID+'&units='+owunit+'&cnt='+cnt+'&lang='+lang).read()
	tree = ET.fromstring(climabruto)
	if param==1:
	#retorna temperatura atual
		tempatual = tree.find('temperature').get('value')
		return(tempatual)
	elif param==2:
	#retorna temperatura minima
		tempmin = tree.find('forecast').find('time').find('temperature').get('min')
		return(tempmin)
	elif param==3:
	#retorna temperatura maxima
		tempmax = tree.find('forecast').find('time').find('temperature').get('max')
		return(tempmax)
	elif param==4:
	#retorna previsao
		previsao = tree.find('forecast').find('time').find('symbol').get('name')
		return(previsao)
	elif param==5:
	#retorna umidade
		umidade = tree.find('forecast').find('time').find('humidity').get('value')
		return(umidade+'%')
	else:
		return("erro")