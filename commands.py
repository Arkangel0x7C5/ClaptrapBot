import datetime
import urllib2

urlbtc = 'https://blockchain.info/es/q/'

def cmdTime():
	return str(datetime.datetime.now())


def btcPrice():
	r = urllib2.urlopen(urlbtc + "24hrprice")
	return r.read()

comands = [cmdTime]

