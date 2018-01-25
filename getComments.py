# -*- coding: utf-8 -*-

import re
import requests
import json

def _read_access_token(filename):
	f = open(filename, 'r')
	data = json.load(f)
	return data["access_token"]

def _read_id(filename):
	f = open(filename, 'r')
	data = json.load(f)
	return (data["page_ID"], data["post_ID"])

def _read_response(res):
	print("Type: {}".format(type(res)))

	Jres = json.loads(res.text)
	Jdata = Jres['data']
	lis = []
	for com in Jdata:
		lis.append(com['message'])
	print 'Recieve {} comments'.format(len(lis))
	if 'next' in Jres['paging']:
		lis = lis + _read_response(requests.get(Jres['paging']['next']))
		
	return lis

def getComments():

	# read page id and post id
	page_id, post_id = _read_id("target.json")
	print page_id
	print post_id

	# read access token
	ACCESS_TOKEN = _read_access_token("meta.json")
	print ACCESS_TOKEN

	# construct URL
	BASE_URL = "https://graph.facebook.com/"
	para_comments = page_id + '_' + post_id + "/" + "comments"
	para_accesstoken = "access_token="+ACCESS_TOKEN
	parameters = para_comments + "?" + para_accesstoken
	url = BASE_URL + parameters
	print url

	# send request / get response
	res = requests.get(url)
	print res

	# read response
	lis = _read_response(res)
	print 'final list' + str(lis)
	return lis
