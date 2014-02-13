#!/usr/bin/python

import sys
import json
import urllib, urllib2
import getopt
from urlparse import urlparse

URL_SHORTENER_API = 'https://www.googleapis.com/urlshortener/v1/url'


PARAMETERS = {
		'source': 'utm_source',
		'medium': 'utm_medium',
		'term': 'utm_term',
		'content': 'utm_content',
		'campaign': 'utm_campaign'
	}


CHANNELS = [
		'LinkedIn',
		'Facebook',
		'Twitter',
		'GooglePlus',
		'Email'
	]


def generate_urls(url, medium=None):
	for channel in CHANNELS:
		print channel + ': ' + generate_url_for_channel(url, channel.lower(), medium)


def generate_url_for_channel(url, source, medium=None):
	concatenated_url = url + '?' + PARAMETERS['source'] + '=' + source + '&' + PARAMETERS['campaign'] + '=' + urlparse(url)[2]
	if medium is not None:
		concatenated_url = concatenated_url + '&' + PARAMETERS['medium'] + '=' + medium
	return shorten_url(concatenated_url)


def shorten_url(url):
	postdata = {'longUrl':url}
	headers = {'Content-Type':'application/json'}
	req = urllib2.Request(
		URL_SHORTENER_API,
		json.dumps(postdata),
		headers
	)
	ret = urllib2.urlopen(req).read()
	#print ret
	return json.loads(ret)['id']


def help():
	print "Help"
	print "ling_generator.py --source <url> --medium=<medium> --campaign==<campaign_name>"
	print "-h --help\t\t\tShow this help message."
	print "-s --source\t\t\tDefine the source url the links will be redirecting to."
	print "-m --medium\t\t\tDefine a specific medium to be dinstiguished in analytics."
	print "-c --campaign\t\t\tDefine the campaign name to be displayed in analytics. By default, the campaign name is <url>."


if __name__ == "__main__":
	#print 'Number of arguments:', len(sys.argv), 'arguments.'
	#print 'Argument List:', str(sys.argv)
	if len(sys.argv) > 2:
		generate_urls(sys.argv[1], sys.argv[2])
	else:
		generate_urls(sys.argv[1])	 

#	try:								
#		opts, args = getopt.getopt(argv, "hs:m:c:", ["help", "source=", "medium=", "campaign="])
#	except getopt.GetoptError:		  
#		sys.exit(2)					 
#	for opt, arg in opts:
#		if opt in ("-h", "--help"):
#			help()					 
#			sys.exit()				  
#		else if opt in ("-s", "--source"):
#			
			#generate_urls(sys.argv[1])
