import datetime
#from urllib import request
import requests
import re
import conf
import json
import random
import codecs

urlbtc = 'https://www.bitstamp.net/api/v2/ticker/'
urlEcoin = 'https://api.coinmarketcap.com/v1/'

frases = {'frases':["no tengo frases, que planeas que diga?"]}
list = []
ecoinList = []


def cmdHola():
	return frases['frases'][random.randint(0,len(frases['frases'])-1)]
def cmdReloadFrases():
	try:
		data_file = codecs.open("frases.json",'r', 'UTF-8').read()
		frases_tmp = json.loads(data_file,'utf8')
		frases.pop('frases',None)
		frases.update(frases_tmp)
		return "frases actualizadas"
	except Exception as e:
		print(e)
def cmdEcoin(msg):
	result = ""
	ecoinList = json.loads(requests.get(urlEcoin + "ticker/?convert=EUR").text,'utf8')
	ecoinName = msg[1];
	
	for coin in ecoinList:
		if ecoinName.upper() == coin["symbol"].upper():
			result += "nombre: "+coin["name"]+" ("+coin["symbol"]+")\n"
			result += "precio:\n"
			result += "    "+coin["price_usd"]+" usd\n"
			result += "    "+coin["price_eur"]+" €\n"
			result += "    "+coin["price_btc"]+" btc\n"
			result += "capitalizacion "+coin["market_cap_usd"]+" usd\n"
			result += "Volumen         "+coin["24h_volume_usd"]+" usd\n"
			result += "Cambio 24h     "+coin["percent_change_24h"]+" usd\n"
			return result
	return "moneda no encotrada"
def cmdTime():
	return str(datetime.datetime.now())
def cmdSource():
	return conf.source

def cmdBtcPrice():
	btcusd = json.loads(requests.get(urlbtc + "btcusd/").text,'utf8')
	btceur = json.loads(requests.get(urlbtc + "btceur/").text,'utf8')
	eurusd = json.loads(requests.get(urlbtc + "eurusd/").text,'utf8')
	return "btc/usd "+btcusd["last"]+"\n"+"btc/eur "+btceur["last"]+"\n"+"usd/eur "+eurusd["last"]+"\n"

def init(botName):
	holaRegex   = re.compile('^(.* )?(\/?(H|h)(ola+|ello|i))[.,!]?(@'+botName+')?( .*)?$')
	timeRegex   = re.compile('^\/(fecha|time)(@'+botName+')? *$')
	ecoinRegex  = re.compile('^\/ecoin(@'+botName+')? +([a-zA-Z]+)$')
	sourceRegex = re.compile('^\/(codigo|source)(@'+botName+')? *$')
	btcPriceRegex = re.compile('\/btc([Pp]rice)?(@'+botName+')? *$')
	reloadFrasesRegex = re.compile('\/(reloadFrases)(@'+botName+')? *$')

	list.extend(	[
			[holaRegex,cmdHola]
			,[timeRegex,cmdTime]
			,[ecoinRegex,cmdEcoin]
			,[sourceRegex,cmdSource]
			,[btcPriceRegex,cmdBtcPrice]
			,[reloadFrasesRegex,cmdReloadFrases]
		])
	cmdReloadFrases()

