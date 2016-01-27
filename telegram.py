#!/usr/bin/env python
#
import json
import urllib
import time

class Bot():
	def __init__(self,
                 token):
		self.token = token
		self.base_url = 'https://api.telegram.org/bot' + self.token
		self.bot = None
		self.offset = None
	def getMe(self):
		url = self.base_url+'/getMe'
		obj = json.loads(urllib.urlopen(url).read())
		if obj['ok'] :
			return obj['result']
	def getUpdates(self):
		url = self.base_url+'/getUpdates'
		if not self.offset is None :
			url = url+'?offset='+str(self.offset) 
		obj = json.loads(urllib.urlopen(url).read())
		if obj['ok'] :
			return obj['result']
	def sendMessage(self,chat_id,text):
		data = {
			'chat_id':chat_id
			,'text':text
			}
		url = self.base_url+'/sendMessage'
		urllib.urlopen(url,urllib.urlencode(data))
		return
	def startPolling(self,handler):
		try:
			while(True):
				for update in self.getUpdates():
					self.offset = update['update_id']+1
					handler(self,update['message'])
				time.sleep(1)
		except KeyboardInterrupt:
			print "Interrupcion de teclado"
		return
