# -*- coding: utf-8 -*-
# @Author: sumansaurabh
# @Date:   2018-06-28 02:27:05
# @Last Modified by:   sumansaurabh
# @Last Modified time: 2018-06-29 22:41:16


import json

_dic={}
_dic_baron={}
_dic_manhattan_essentials={}

with open('baron-final.json') as outfile:
	_dic_baron=json.load(outfile)


with open('manhattan-essentials-final.json') as outfile:
	_dic_manhattan_essentials=json.load(outfile)


_dic_baron={**_dic_baron, **_dic_manhattan_essentials}

print(len(_dic_baron.keys()))



def load_json(idx):
	global _dic
	global _dic_baron

	with open('mahattan-advanced-'+str(idx)+'.json') as outfile:
		k=json.load(outfile)

		for itm in k:
			if not itm in _dic_baron:
				_dic[itm]=k[itm]



		# _dic={**_dic, **k}
		# print(_dic)



for i in range(1,51):
	load_json(i)
	# break

print(len(_dic.keys()))

print(_dic.keys())





with open('manhattan-advanced-final.json', 'w') as outfile:
	json.dump(_dic, outfile)

