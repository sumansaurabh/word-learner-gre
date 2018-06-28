# -*- coding: utf-8 -*-
# @Author: sumansaurabh
# @Date:   2018-06-28 02:27:05
# @Last Modified by:   sumansaurabh
# @Last Modified time: 2018-06-28 02:35:50


import json

_dic={}
def load_json(idx):
	global _dic
	with open('baron-pg-'+str(idx)+'.json') as outfile:
		k=json.load(outfile)
		_dic={**_dic, **k}
		# print(_dic)



for i in range(1,47):
	load_json(i)
	# break

print(len(_dic.keys()))

with open('baron-final.json', 'w') as outfile:
	json.dump(_dic, outfile)
