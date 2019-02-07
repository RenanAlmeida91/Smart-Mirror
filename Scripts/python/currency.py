#BUSCA CAMBIO YAHOO
#==================
#importa bibliotecas:
import urllib
import xml.etree.ElementTree as ET

#define a URL e parametros
yahoourl = "https://query.yahooapis.com/v1/public/yql?q="
moedaquery = 'select * from yahoo.finance.xchange where pair in ("'
moedaformat = "xml"
moedaenv = "store://datatables.org/alltableswithkeys"

#busca na web e retorna
def buscamoeda(moeda):
	moedaquery_encoded = urllib.quote(moedaquery+moeda+'BRL")')
	moedaformat_encoded = urllib.quote(moedaformat)
	moedaenv_encoded = urllib.quote(moedaenv)
	moedabruto = urllib.urlopen(yahoourl+moedaquery_encoded+'&format='+moedaformat_encoded+'&env='+moedaenv_encoded).read()
	#analise do xml obtido
	tree = ET.fromstring(moedabruto)
	nomecotacao = tree.find('results').find('rate').find('Name').text
	cotacao = tree.find('results').find('rate').find('Rate').text
	#retorna valor no formato MOEDA=VALOR
	return(cotacao)