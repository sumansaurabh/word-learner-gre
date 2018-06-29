# -*- coding: utf-8 -*-
# @Author: sumansaurabh
# @Date:   2018-06-28 02:27:05
# @Last Modified by:   sumansaurabh
# @Last Modified time: 2018-06-29 21:56:49


import json

_dic={}
_dic_baron={}
_dic_manhattan_essentials={}
_dic_manhattan_advanced={}


with open('baron-final.json') as outfile:
	_dic_baron=json.load(outfile)


with open('manhattan-essentials-final.json') as outfile:
	_dic_manhattan_essentials=json.load(outfile)

with open('manhattan-advanced-final.json') as outfile:
	_dic_manhattan_advanced=json.load(outfile)

_dic_baron={**_dic_baron, **_dic_manhattan_essentials}
_dic_baron={**_dic_baron, **_dic_manhattan_advanced}
print(len(_dic_baron.keys()))



def load_json(idx):
	global _dic
	global _dic_baron

	with open('magoosh-'+str(idx)+'.json') as outfile:
		k=json.load(outfile)

		for itm in k:
			if not itm in _dic_baron:
				_dic[itm]=k[itm]



		# _dic={**_dic, **k}
		# print(_dic)



for i in range(1,32):
	load_json(i)
	# break

print(len(_dic.keys()))

print(_dic.keys())





with open('magoosh-final.json', 'w') as outfile:
	json.dump(_dic, outfile)

