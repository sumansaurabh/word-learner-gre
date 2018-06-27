# -*- coding: utf-8 -*-
# @Author: perfectus
# @Date:   2018-06-27 20:00:24
# @Last Modified by:   perfectus
# @Last Modified time: 2018-06-27 20:57:13

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

with open('words.json') as f:
    data = json.load(f)


for itm in data:
	url="http://localhost:5000/api/add"

	payload={
		"word" : itm,
		"meaning": data[itm]
	}

	headers = {
		"Content-Type" : "application/json",
	}
	r = requests.post(url, headers=headers, data = json.dumps(payload))

	a = json.dumps(r.text)
	b = json.loads(a)

	# print("itm -> ",itm)
	# print(b)