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
        print '�Ҳ�����Ҫ��ȡ���ļ�����������ȷ���ļ���...'

    
def writeline(filename,str):
    try:
        file = open(filename,'a')
        file.write(str+'\n')
    except:
        print 'Error......'
    finally:
        file.close()

if __name__ == "__main__":
    filename = raw_input('�������ļ�����')    
    str = raw_input('��������������ǣ�')
    writeline(filename,str)
    file = raw_input('��������Ҫ���ҵ��ļ�����')
    lines = raw_input('��������������ǣ�')
    lines = int(lines)
    readline(file,lines)

