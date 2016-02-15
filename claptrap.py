#!/usr/bin/env python3

import time
import telegram
import re
import conf
import commands
import json
import logging
import os
import sys


os.chdir(os.path.dirname(os.path.realpath(__file__)))

logging.basicConfig(level=logging.DEBUG)
handler = logging.FileHandler('debug.log', 'w', 'utf-8')

root_logger= logging.getLogger()
root_logger.addHandler(handler)

logger = logging.getLogger('claptrap')

bot = telegram.Bot(conf.botID)

commands.init(bot.getMe()['username'])


def handle(bot,msg):
	logger.debug(json.dumps(msg)+"\n")
	#if not msg.has_key("text") and not msg.has_key("chat"):
	try:	
		#logging.debug("test\n")
		chat_id = msg['chat']['id']
		text	= msg['text']
	
		logger.info("Mensaje recibido: "+ text)
	
		for comando in commands.list:
			if comando[0].match(text):
				bot.sendMessage(chat_id,comando[1]())
				return
		#bot.sendMessage(chat_id,"test")
	except KeyError:
		return

#bot.notifyOnMessage(callback=handle, run_forever=True)
try:
	bot.startPolling(handle)
except e:
	logger.error(e)
#while(1):
#	time.sleep(10)
