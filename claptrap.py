import time
import telepot
import datetime
import re
import conf
import commands
import json
import logging
import os
import sys

os.chdir(os.path.dirname(os.path.realpath(__file__)))

logging.basicConfig(filename='debug.log',level=logging.DEBUG)
bot = telepot.Bot(conf.botID)
botName = bot.getMe()['username']
frases = ["no tengo frases, que planeas que diga?"]

holaRegex   = re.compile('^\/hola(@'+botName+')? *$')
timeRegex   = re.compile('^\/time(@'+botName+')? *$')
sourceRegex = re.compile('^\/source(@'+botName+')? *$')
btcPriceRegex = re.compile('\/btc([Pp]rice)?(@'+botName+')? *$')


def handle(msg):
	logging.debug(json.dumps(msg)+"\n")
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
		#bot.sendMessage(chat_id,btcPrice())
		bot.sendMessage(chat_id,commands.btcPrice())

bot.notifyOnMessage(handle)

while 1:
	time.sleep(10)
