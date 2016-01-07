import time
import telepot
import datetime
import re
import conf
import commands

#######
# BTC #
#######
import urllib2

urlbtc = 'https://blockchain.info/es/q/'

def btcPrice():
	r = urllib2.urlopen(urlbtc + "24hrprice")
	return r.read()

bot = telepot.Bot(conf.botID)
botName = bot.getMe()['username']
frases = ["no tengo frases, que planeas que diga?"]

holaRegex   = re.compile('^\/hola(@'+botName+')? *$')
timeRegex   = re.compile('^\/time(@'+botName+')? *$')
sourceRegex = re.compile('^\/source(@'+botName+')? *$')
btcPriceRegex = re.compile('\/btcPrice(@'+botName+')? *$')


def handle(msg):
	if not msg.has_key("text") and not msg.has_key("chat"):
		return
	chat_id = msg['chat']['id']
	command = msg['text']
	print 'Mensage recibido: %s' % command
	if timeRegex.match(command):
		bot.sendMessage(chat_id,str(datetime.datetime.now()))
	elif holaRegex.match(command):
		bot.sendMessage(chat_id,frases[0])
	elif sourceRegex.match(command):
		bot.sendMessage(chat_id,conf.source)
	elif btcPriceRegex.match(command):
		bot.sendMessage(chat_id,btcPrice())		

bot.notifyOnMessage(handle)

while 1:
	time.sleep(10)
