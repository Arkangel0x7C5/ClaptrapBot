import time
import telepot
import datetime
import re
import conf
import commands

bot = telepot.Bot(conf.botID)
frases = ["no tengo frases, que planeas que diga?"]
holaRegex = re.compile('^\/hola(@claptrap_hsec_bot)? *$')
timeRegex = re.compile('^\/time(@claptrap_hsec_bot)? *$')


def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']
	print 'Mensage recibido: %s' % command
	if timeRegex.match(command):
		bot.sendMessage(chat_id,str(datetime.datetime.now()))
	elif holaRegex.match(command):
		bot.sendMessage(chat_id,frases[0])

bot.notifyOnMessage(handle)

while 1:
	time.sleep(10)
