# -*- coding:utf-8 -*-
import os
import os.path
import re
import sys
import codecs
import shutil
from datetime import datetime

Path = 'J:'

def list_all_files(rootdir):
    _files = []
    files = os.listdir(rootdir) #�г��ļ��������е�Ŀ¼���ļ�
    # print(files)
    for i in range(0,len(files)):
           path = os.path.join(rootdir,files[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
              _files.append(path)
    return _files

def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   #�ж��Ƿ�����ļ�������������򴴽�Ϊ�ļ���
		os.makedirs(path)            #makedirs �����ļ�ʱ���·�������ڻᴴ�����·��
		print( "---  new folder...  ---")
 
	else:
		print( "---  There is this folder!  ---")

def copy_file_to_disk_hidden(FILE_PATH):
    # U�̵��̷�
    file_path = FILE_PATH
    save_path = "L:" + "\\" + Path[0] + "_copy"  

    pattern = Path + r'(.*?)(.*)\\'
    mm = re.findall(pattern, file_path )
    print(file_path, mm[0][1])
    if mm:
    	create_file = '\\'  + mm[0][1]
    	save_path = save_path + create_file

    if os.path.exists(file_path):
    	# shutil.copy(file_path, os.path.join(save_path, datetime.now().strftime("%Y%m%d_%H%M%S")))
    	if mm:
    		mkdir(save_path )

    	shutil.copy(file_path, save_path )
    else:
    	print("path not exist")


# files = os.listdir(Path)
# # print(files)

f = list_all_files(Path) 
print('------>' )
# print(f)
for i in range(0 , len(f)):
	ff = f[i].split('\\')[-1]
	# print(ff)
	# print( ff.split('.')[-1]  )
	if ff.split('.')[-1] == 'doc' :
		print(f[i])
		copy_file_to_disk_hidden(f[i])