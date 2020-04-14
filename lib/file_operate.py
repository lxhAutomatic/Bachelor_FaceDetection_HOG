# -*- coding: utf-8 -*-

import os
import numpy as np

def find_all_picture(path):
    name=[]
    for filename in os.listdir(path):
        if filename.endswith('jpg') :
            name.append(filename)
    return name

def mk_folder(path):   #创建文件夹
 	folder = os.path.exists(path)
 	if not folder:                           #判断是否存在文件夹如果不存在则创建为文件夹
		 os.makedirs(path) 
        
def write_lists(lists,path): #输入一个多维数组并且储存到文件
    output = open(path,'w+')
    for i in range(len(lists)):
	    for j in range(len(lists[i][0])):
		    output.write(str(lists[i][0][j]))
		    output.write(' ')   
	    output.write('\n')      
    output.close()

def add_ndarray(ndarray,path):
    output = open(path,'a+')
    lists=list(ndarray)
    for i in range(len(lists)):
        output.write(str(lists[i]))
        output.write(' ')
    output.write('\n') 
    output.close()
    
def read_lists(path):       #从文件中读取多维数组,返回ndarray类型
    file=open(path, 'r')
    list_read =file.readlines()
    for i in range(len(list_read)):
        #list_read[i]=float(list_read[i].split())
        list_read[i]=[float(j) for j in list_read[i].split()]
    return np.array(list_read)

def read_np_lists(path):       #从文件中读取多维数组,返回ndarray类型
    file=open(path, 'r')
    list_read =file.readlines()
    for i in range(len(list_read)):
        #list_read[i]=float(list_read[i].split())
        list_read[i]=[np.float32(j) for j in list_read[i].split()]
    return np.array(list_read)
