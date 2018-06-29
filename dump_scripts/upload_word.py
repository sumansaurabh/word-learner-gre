# -*- coding: utf-8 -*-
# @Author: perfectus
# @Date:   2018-06-27 20:00:24
# @Last Modified by:   sumansaurabh
# @Last Modified time: 2018-06-29 23:40:33

# words={}

# with open("words.dat") as inp:
#     for line in inp:
#         word, definition = line.strip("\r\n").split("\t", 1)

#         words[word] = definition


# print(words)

# import json
# with open('words.json', 'w') as outfile:
#     json.dump(words, outfile)

import json
import requests
from pprint import pprint
import re
# with open('baron-final.json') as f:
#     data = json.load(f)


# def new_str(_str):
# 	new_str=""
# 	idx=0
# 	for ch in _str:
# 		if ch!='/':
# 			new_str += ch

# 		else:
# 			break
# 		idx+=1

	
# 	new_idx=-1
# 	for i in range(idx+1, len(_str)):
# 		ch=_str[i]
# 		if ch==' ' or ch=='/':
# 			continue
# 		new_idx=i
# 		break
# 	if new_idx != -1:
# 		return new_str+"/"+_str[new_idx+1:]
# 	return new_str





# for itm in data:
# 	url="http://localhost:5000/api/add"
# 	data[itm]=re.sub(r'[^\x00-\x7F]+','', data[itm])
# 	# data[itm]=new_str(data[itm])
# 	payload={
# 		"word" : itm,
# 		"meaning": data[itm],
# 		"word_type": word_type
# 	}

# 	# pprint(payload)

# 	headers = {
# 		"Content-Type" : "application/json",
# 	}
# 	r = requests.post(url, headers=headers, data = json.dumps(payload))

# 	a = json.dumps(r.text)
# 	b = json.loads(a)

# 	# print("itm -> ",itm)
# 	# print(b)


word_list=[{
	"id": "baron",
	"loc": "baron/baron-final.json"   
},{
	"id": "magoosh",
	"loc": "magoosh/magoosh-final.json"   
},{
	"id": "manhattan_essentials",
	"loc": "manhattan-essentials/manhattan-essentials-final.json"   
},{
	"id": "manhattan_advanced",
	"loc": "manhattan-advanced/manhattan-advanced-final.json"   
}];


def append_data_to_db(id, loc):
	print("working on->",id)
	with open(loc) as f:
		data = json.load(f)


	for itm in data:
		url="http://localhost:5000/api/add"
		payload={
			"word" : itm,
			"meaning": data[itm],
			"word_type": id
		}

		# pprint(payload)

		headers = {
			"Content-Type" : "application/json",
		}
		r = requests.post(url, headers=headers, data = json.dumps(payload))

		a = json.dumps(r.text)
		b = json.loads(a)

word_list=word_list[2:]
for itm in word_list:
	append_data_to_db(itm['id'], itm['loc'])