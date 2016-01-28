#!/usr/bin/env python3
#
import json
from urllib import request 
from urllib import parse
import time
import logging

class Bot():
	def __init__(self,
                 token):
		self.token = token
		self.base_url = 'https://api.telegram.org/bot' + self.token
		self.bot = None
		self.offset = None
	def getMe(self):
		url = self.base_url+'/getMe'
		obj = json.loads(request.urlopen(url).read().decode('utf8'))
		if obj['ok'] :
			return obj['result']
	def getUpdates(self):
		url = self.base_url+'/getUpdates'
		if not self.offset is None :
			url = url+'?offset='+str(self.offset) 
		obj = json.loads(request.urlopen(url).read().decode('utf8'))
		if obj['ok'] :
			return obj['result']
	def sendMessage(self,chat_id,text):
		data = {
			'chat_id':chat_id
			,'text':text
			}
		url = self.base_url+'/sendMessage'
		request.urlopen(url,parse.urlencode(data).encode('utf8'))
		return
	def startPolling(self,handler):
		try:
			while(True):
				try:
					for update in self.getUpdates():
						self.offset = update['update_id']+1
						if 'message' in update :
							handler(self,update['message'])
				except IOError:
					pass
				time.sleep(1)
		except KeyboardInterrupt:
			print("Interrupcion de teclado")
		except Exception as e:
			logging.exception(e)
			
		return
