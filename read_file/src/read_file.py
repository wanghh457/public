#!/usr/local/bin/python  
# -*- coding:cp850 -*-  

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="whh"
__date__ ="$2014-10-9 13:09:59$"


def readline(filename,lines):
    import linecache
    try:
        file = open(filename,'r')
        print(linecache.getline(filename,lines))
    except:
        print '找不到您要读取的文件！请输入正确的文件名...'

    
def writeline(filename,str):
    try:
        file = open(filename,'a')
        file.write(str+'\n')
    except:
        print 'Error......'
    finally:
        file.close()

if __name__ == "__main__":
    filename = raw_input('请输入文件名：')    
    str = raw_input('您想输入的内容是：')
    writeline(filename,str)
    file = raw_input('请输入您要查找的文件名：')
    lines = raw_input('您想输出的行数是：')
    lines = int(lines)
    readline(file,lines)

