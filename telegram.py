#!/usr/bin/env python3

import json
import time
import logging
import requests

class Bot():
	def __init__(self,
                 token):
		self.token = token
		self.base_url = 'https://api.telegram.org/bot' + self.token
		self.bot = None
		self.offset = None
#		self.headers = {'content-type':'application/json; charset=utf-8'}
		self.logger = logging.getLogger('telegram')
		
		urllib3_logger = logging.getLogger('urllib3')
		urllib3_logger.setLevel(logging.CRITICAL)
	def getMe(self):
		url = self.base_url+'/getMe'
		obj = requests.get(url).json()
#		obj = json.loads(request.urlopen(url).read().decode('utf8'))
		if obj['ok'] :
			return obj['result']
	def getUpdates(self):
		url = self.base_url+'/getUpdates'
		params = {}
		if not self.offset is None :
			params = {'offset':self.offset}
		try:
			obj = requests.get(url,params=params).json()
			if obj['ok']:
				return obj['result']
		except Exception:
			pass
		return []
	def sendMessage(self,chat_id,text):
		data = {
			'chat_id':chat_id
			,'text':text
			}
		url = self.base_url+'/sendMessage'
		requests.post(url,data = data)
		return
	def startPolling(self,handler):
		try:
			while(True):
				try:
					for update in self.getUpdates():
						self.offset = update['update_id']+1
						if 'message' in update :
							handler(self,update['message'])
				except IOError as e:
					self.logger.exception(e)
				time.sleep(1)
		except KeyboardInterrupt:
			#print("Interrupcion de teclado")
			pass
		except Exception as e:
			self.logger.exception(e)
		return
