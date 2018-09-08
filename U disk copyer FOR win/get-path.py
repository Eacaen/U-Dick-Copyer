# -*- coding:utf-8 -*-
import re , os
from datetime import datetime

P  = "L:"
P2 = "J:"
P1 = "J:\\taiwan visa2\\rutaizheng\\3.hh\\7.hhhhhhhh.doc"

# pattern = re.compile(P2+r'/.*?/')   # re.I 表示忽略大小写
pattern = P2 + r'(.*?)(.*)\\'
mm = re.findall(pattern, P1 )

for value in mm:
	print(value)

print(mm[0])
print(mm[0][1])

def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print( "---  new folder...  ---")
 
	else:
		print( "---  There is this folder!  ---")

mkdir(P + "\\" + P2[0] + "_copy" + mm[0][1])