#!/usr/bin/python

import sys
import json
import urllib, urllib2


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
	concatenated_url = url + '?' + PARAMETERS['source'] + '=' + source + '&' + PARAMETERS['campaign'] + '=' + url
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


if __name__ == "__main__":
	#print 'Number of arguments:', len(sys.argv), 'arguments.'
	#print 'Argument List:', str(sys.argv)
	if len(sys.argv) > 2:
		generate_urls(sys.argv[1], sys.argv[2])
	else:
		generate_urls(sys.argv[1])     
