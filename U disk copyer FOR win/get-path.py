# -*- coding:utf-8 -*-
import re , os
from datetime import datetime

P  = "L:"
P2 = "J:"
P1 = "J:\\taiwan visa2\\rutaizheng\\3.hh\\7.hhhhhhhh.doc"

# pattern = re.compile(P2+r'/.*?/')   # re.I ��ʾ���Դ�Сд
pattern = P2 + r'(.*?)(.*)\\'
mm = re.findall(pattern, P1 )

for value in mm:
	print(value)

print(mm[0])
print(mm[0][1])

def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   #�ж��Ƿ�����ļ�������������򴴽�Ϊ�ļ���
		os.makedirs(path)            #makedirs �����ļ�ʱ���·�������ڻᴴ�����·��
		print( "---  new folder...  ---")
 
	else:
		print( "---  There is this folder!  ---")

mkdir(P + "\\" + P2[0] + "_copy" + mm[0][1])