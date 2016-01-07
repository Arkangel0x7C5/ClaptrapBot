import datetime
import conf
import urllib2

def cmdTime():
	return str(datetime.datetime.now())


def btcPrice():
	r = urllib2.urlopen(conf.urlbtc + "24hrprice")
	return r.read()

comands = [cmdTime]

