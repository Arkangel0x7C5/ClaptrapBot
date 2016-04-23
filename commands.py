import datetime
#from urllib import request
import requests
import re
import conf
import json
import random
import codecs

urlbtc = 'https://blockchain.info/es/q/'

frases = {'frases':["no tengo frases, que planeas que diga?"]}
list = []

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
def cmdTime():
	return str(datetime.datetime.now())
def cmdSource():
	return conf.source

def cmdBtcPrice():
	r = requests.get(urlbtc + "24hrprice")
	return r.text

def init(botName):
	holaRegex   = re.compile('^(.* )?(\/?(H|h)(ola+|ello|i))[.,!]?(@'+botName+')?( .*)?$')
	timeRegex   = re.compile('^\/(fecha|time)(@'+botName+')? *$')
	sourceRegex = re.compile('^\/(codigo|source)(@'+botName+')? *$')
	btcPriceRegex = re.compile('\/btc([Pp]rice)?(@'+botName+')? *$')
	reloadFrasesRegex = re.compile('\/(reloadFrases)(@'+botName+')? *$')

	list.extend(	[
			[holaRegex,cmdHola]
			,[timeRegex,cmdTime]
			,[sourceRegex,cmdSource]
			,[btcPriceRegex,cmdBtcPrice]
			,[reloadFrasesRegex,cmdReloadFrases]
		])
	cmdReloadFrases()

