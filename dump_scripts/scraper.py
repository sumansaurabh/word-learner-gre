# -*- coding: utf-8 -*-
# @Author: sumansaurabh
# @Date:   2018-06-28 02:01:29
# @Last Modified by:   sumansaurabh
# @Last Modified time: 2018-06-28 02:25:04

import requests
from bs4 import BeautifulSoup



# url="https://www.memrise.com/course/127378/barrons-1100-words-you-need-to-know-2/1/"
# html=requests.get(url)
# soup = BeautifulSoup(html.text, 'html.parser')

# print(soup.prettify())

# print("############################")
# print("############################")
# print("############################")
# print("############################")
# print("############################")

# _dic={}

# for itm in soup.findAll('div', attrs={'class':'text-text'}):
# 	# print(itm)
# 	print("---->")
# 	count=0
# 	key=""
# 	for child in itm.children:
# 		if count==2:
# 			print(child.string)
# 			key=child.string
			
# 		if count==3:
# 			_dic[key]=child.string
# 			print(child.string)
# 		count+=1
# 	# print(itm.children[2].string)


# import json
# with open('baron-pg-1.json', 'w') as outfile:
#     json.dump(_dic, outfile)
	

def scrape(url, idx):
	url="https://www.memrise.com/course/127378/barrons-1100-words-you-need-to-know-2/"+str(idx)+"/"
	html=requests.get(url)
	soup = BeautifulSoup(html.text, 'html.parser')

	print(soup.prettify())

	print("############################")
	print("############################")
	print("############################")
	print("############################")
	print("############################")

	_dic={}

	for itm in soup.findAll('div', attrs={'class':'text-text'}):
		# print(itm)
		print("---->")
		count=0
		key=""
		for child in itm.children:
			if count==2:
				print(child.string)
				key=child.string
				
			if count==3:
				_dic[key]=child.string
				print(child.string)
			count+=1
		# print(itm.children[2].string)


	import json
	with open('baron/baron-pg-'+str(idx)+'.json', 'w') as outfile:
	    json.dump(_dic, outfile)

for i in range(1,47):

	scrape("",i)