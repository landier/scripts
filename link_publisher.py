#!/usr/bin/python

import sys
import json
import urllib, urllib2

API_KEY = ''

URL_SHORTENER_API = 'https://www.googleapis.com/urlshortener/v1/url'


EXAMPLE = 'http://www.urchin.com/download.html?utm_source=SOURCE&utm_medium=SUPPORT&utm_term=TERME&utm_content=CONTENU&utm_campaign=NOM'


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
		'Email'
	]


def generate_urls(url):
	for channel in CHANNELS:
		print channel + ': ' + generate_url_for_channel(url, channel.lower())

def generate_url_for_channel(url, source):
	concatenated_url = url + '?' + PARAMETERS['source'] + '=' + source + '&' + PARAMETERS['campaign'] + '=' + url
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


if __name__ == "__main__":
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)
	generate_urls(sys.argv[1])
	shorten_url('http://nicolas.landier.org')
