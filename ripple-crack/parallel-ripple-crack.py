# -*- coding: utf-8 -*-
#!/usr/bin/python
#test_copyfile.py

import os,shutil,time

driver = 'E:/'
pass_dir = '..//pass'
time_split = 5
def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!"%(srcfile)
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        #print "move %s -> %s"%( srcfile,dstfile)
def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!"%(srcfile)
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        #print "copy %s -> %s"%( srcfile,dstfile)

def file_name(src_file_dir,dst_file_dir):   
    for root, dirs, files in os.walk(src_file_dir):
        if  len(files) ==0:
            print 'file not found ,please check !!!'  
        for name in files:
            src_file_path = '%s%s%s' % (src_file_dir,'/',name)
            dst_file_path = '%s%s%s' % (dst_file_dir,'/',name)
            #print src_file_path#当前路径下所有非目录子文件
            mymovefile(src_file_path,dst_file_path)
            #mycopyfile(src_file_path,dst_file_path)
def  del_file(path):
    if os.path.exists(path):
        shutil.rmtree(path)


while True: 
    #清空缓存文件
    time.sleep(3)
    del_file(driver+"crack_tmp/")
    del_file(driver+"crack_split/")     
    #从字典池取文件
    file_name(pass_dir,driver+"crack_tmp")

    #进行分组
    #获取剪切后的所有文件
    files_name_all =[]
    for root, dirs, files_name_all in os.walk(driver+"crack_tmp"):
        pass
        #print files_name_all
    #分成5组
    split_result = [[],[],[],[],[]]
    split_count = len(files_name_all)/5
    for item in files_name_all:
            if len(split_result[0]) < split_count:
                    split_result[0].append(item)
            elif len(split_result[1]) < split_count:
                    split_result[1].append(item)
            elif len(split_result[2]) < split_count:
                    split_result[2].append(item)
            elif len(split_result[3]) < split_count:
                    split_result[3].append(item)
            else:
                    split_result[4].append(item)
    #print split_result
    for index in range(0,5):
        mycopyfile("./Driver.exe",driver+"crack_split/"+str(index)+"/Driver.exe")
        mycopyfile("./callcmd.exe",driver+"crack_split/"+str(index)+"/callcmd.exe")
        #复制每一组
        for file_name_per in  split_result[index]:
                src_file_path = '%s%s%s' % (driver+"crack_tmp",'/',file_name_per)
                dst_file_path = '%s%s%s%s' % (driver+"crack_split/",str(index),"/pass/",file_name_per)
                mymovefile(src_file_path,dst_file_path)
    for index in range(0,5):
        dst_file_path = driver+"crack_split/"+str(index)+"/callcmd.exe"
        pass_dst_file_path = '%s%s%s' % (driver+"crack_split/",str(index),"/pass/")
        if os.path.exists(pass_dst_file_path):
            os.system(dst_file_path+' Driver.exe '+pass_dst_file_path)
    while True:
        time.sleep(time_split)
        count = 0        
        for index in range(0,5):
            pass_dst_file_path=driver+"crack_split/"+str(index)+"/pass/"
            dst_file_path = pass_dst_file_path+"/done"
            if not os.path.exists(pass_dst_file_path):
                count+=1
            if not os.path.exists(dst_file_path):
                continue
            else:
                count+=1
        if count==5:
            break

#print files_name_all
#运行程序