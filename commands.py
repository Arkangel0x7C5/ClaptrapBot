import datetime
from urllib.request import urlopen
import re
import conf

urlbtc = 'https://blockchain.info/es/q/'

frases = ["no tengo frases, que planeas que diga?"]
list = []

def cmdHola():
	return frases[0]
def cmdTime():
	return str(datetime.datetime.now())
def cmdSource():
	return conf.source

def cmdBtcPrice():
	r = urlopen(urlbtc + "24hrprice")
	return r.read()

def init(botName):
	holaRegex   = re.compile('^(hola|\/(hola|hello))(@'+botName+')? *$')
	timeRegex   = re.compile('^\/(fecha|time)(@'+botName+')? *$')
	sourceRegex = re.compile('^\/(codigo|source)(@'+botName+')? *$')
<<<<<<< HEAD
=======

>>>>>>> 62dfffa88f8b1b88a5f024c87de98d9a275554da
	btcPriceRegex = re.compile('\/btc([Pp]rice)?(@'+botName+')? *$')
	
	list.extend(	[
			[holaRegex,cmdHola]
			,[timeRegex,cmdTime]
			,[sourceRegex,cmdSource]
			,[btcPriceRegex,cmdBtcPrice]
		])
