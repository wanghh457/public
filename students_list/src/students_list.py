#!/usr/local/bin/python  
# -*- coding:cp850 -*-  
  
import os  
import re  
  
#����ѧ����  
class Student:  
    def __init__(self):  
        self.name = ''  
        self.ID = ''  
        self.score = 0  
  
#����ѧ���������дӴ�С��ð������  
def BuddleSortByScore( stulist ):  
    n = len( stulist )  
    for i in range( n ):  
        for j in range( n - i - 1):  
            if stulist[j].score < stulist[j+1].score:  
                #tmp = stulist[j+1]  
                #stulist[j+1] = stulist[j]  
                #stulist[j] = tmp  
                stulist[j],stulist[j+1] = stulist[j+1],stulist[j]  
  
#��˳���������ѧ������Ϣ  
def PrintAllStudentInfo( stulist ):  
    print "______________________ѧ���б�_______________"  
    for i in range( len(stulist) ):  
        print "����:" ,  
        print stulist[i].name,  
        print "    " ,  
        print "ѧ��:" ,  
        print stulist[i].ID ,  
        print "   " ,  
        print "������" ,  
        print stulist[i].score  
    print "____________________________________________"  
  
#����һ��ѧ��,���ӳɹ�����True�����򷵻�False  
def Add( stulist , stu ):  
    if searchByID( stulist , stu.ID ) == 1:  
        print "��ID�Ѿ����ڣ�"  
        return False  
    stulist.append( stu )  
  
    #�����Ƿ񱣴�������ݵ�ѡ��  
    print "Do you want to save the result ?"  
    nChoose = raw_input("Choose:Y/N:")  
      
    if nChoose == 'Y' or nChoose == 'y':  
        #���ı��Ľ��д���ļ���,׷��д�ļ�  
        file_object = open("students.txt","a")  
        file_object.write( stu.ID )  
        file_object.write( " " )  
        file_object.write( stu.name )  
        file_object.write( " " )  
        file_object.write( str(stu.score) )  
        file_object.write( "\r\n" )  
        file_object.close()  
        return True  
    else:  
        stulist.remove(stu)  
  
#����IDɾ��һ��ѧ������Ϣ��ɾ���ɹ��򷵻�True�����򷵻�false  
def DeleteByID( stulist , ID ):  
    for stu in stulist:  
        if stu.ID == ID:  
            stulist.remove( stu )  
  
            #ѡ���Ƿ񱣴��Ѿ��ı������  
            print "Do you want to save the changed result ?"  
            nChoose = raw_input("Choose:Y/N:")  
              
            if nChoose == 'Y' or nChoose == 'y':  
                file_object = open("students.txt" , "w+")  
                for stu2 in stulist:  
                    file_object.write(stu2.ID)  
                    file_object.write(" ")  
                    file_object.write(stu2.name)  
                    file_object.write(" ")  
                    file_object.write(str(stu2.score))  
                    file_object.write("\r\n")  
                file_object.close()  
                print "ɾ���ɹ�!"  
            return True  
    print "ɾ��ʧ��!"  
    return False  
  
  
#��������ɾ��һ��ѧ������Ϣ��ɾ���ɹ�����True,���򷵻�False  
def DeleteByName( stulist , name ):  
    pos = searchByName( stulist , name )  
    if pos != -1:  
        del stulist[pos]  
  
        #ѡ���Ƿ񱣴��Ѿ��ı������  
        print "Do you want to save the changed result ?"  
        nChoose = raw_input("Choose:Y/N:")  
              
        if nChoose == 'Y' or nChoose == 'y':  
             file_object = open("students.txt" , "w+")  
             for stu2 in stulist:  
                 file_object.write(stu2.ID)  
                 file_object.write(" ")  
                 file_object.write(stu2.name)  
                 file_object.write(" ")  
                 file_object.write(str(stu2.score))  
                 file_object.write("\r\n")  
             file_object.close()  
             print "ɾ���ɹ�!"  
        return True  
    else:  
        print "ɾ��ʧ��!"  
        print pos  
        return False  
  
  
#����ѧ�Ų���һ��ѧ���Ƿ����,���ڷ���ѧ�����б��е��±꣬���򷵻�-1  
def searchByID( stulist , ID ):  
    for i in range( len(stulist) ):  
        if stulist[i].ID == ID:  
            print "������" ,  
            print stulist[i].name ,  
            print "  " ,  
            print "ѧ��:" ,  
            print stulist[i].ID ,  
            print "   " ,  
            print "����:" ,  
            print stulist[i].score   
            return i  
    return -1  
  
#������������һ��ѧ���Ƿ���ڣ����ڷ���ѧ�����б��е��±�,���򷵻�-1  
def searchByName( stulist , name ):  
    for i in range( len(stulist) ):  
        if stulist[i].name == name:  
            print "������" ,  
            print stulist[i].name ,  
            print "  " ,  
            print "ѧ��:" ,  
            print stulist[i].ID ,  
            print "   " ,  
            print "����:" ,  
            print stulist[i].score   
            return i  
    return -1  
  
#��ʼ������ȡ�ļ�������ѧ����Ϣ  
def Init( stulist ):  
    print "��ʼ��......"  
      
    file_object = open("students.txt","r")  
  
    #���ж�ȡ�ļ���ѧ������Ϣ  
    for line in file_object:  
        stu = Student()  
        line = line.strip("\n")  
        s = line.split(" ")  
        stu.ID = s[0]  
        stu.name = s[1]  
        stu.score = s[2]  
        stulist.append(stu)  
    print "��ʼ���ɹ�!"  
                         
  
#���Ҳ˵�  
def QueryMenu( stulist ):  
    while True:  
        print "******************************"  
        print "����ѧ����ѧ�Ž��в���-------1"  
        print "����ѧ�����������в���-------2"  
        print "�뿪����ģ��----------------3"  
        print "******************************"  
  
        nChoose = raw_input("���������ѡ��")  
  
        if nChoose == "1":  
            ID = raw_input("��������Ҫ������ҵ�ID:")  
            searchByID( stulist , ID )  
        elif nChoose == "2":  
            name = raw_input("��������Ҫ���ҵ�����:")  
            searchByName( stulist , name )  
        elif nChoose == "3":  
            return  
        else:  
            print "ѡ�������������������!"  
              
#ɾ��ģ��  
def DeleteMenu( stulist ):  
    while True:  
        print "*****************************"  
        print "����ѧ����ѧ�Ž���ɾ��------1"  
        print "����ѧ������������ɾ��------2"  
        print "�뿪ɾ��ģ��---------------3"  
        print "******************************"  
  
        nChoose = raw_input("�����ѡ��:")  
  
        if nChoose == "1":  
            ID = raw_input("��������Ҫɾ����ID:")  
            DeleteByID( stulist , ID )  
        elif nChoose == "2":  
            name = raw_input("��������Ҫɾ��������:")  
            DeleteByName( stulist , name )  
        elif nChoose == "3":  
            return  
        else:  
            print "����ѡ���������������룡"  
              
                          
#�˵�  
def menu( stulist ):  
    while True:  
        print "***********************"  
        print "--------�˵�------------"  
        print "����ѧ����Ϣ---------1"  
        print "����һ��ѧ������Ϣ----2"  
        print "ɾ��һ��ѧ������Ϣ----3"  
        print "�������ѧ������Ϣ----4"  
        print "���ݷ�������---------5"  
        print "�˳�����-------------6"  
        print "------------------------"  
        print "************************"  
  
        nChoose = raw_input("���������ѡ��:")  
          
        if nChoose == "1":  
            stu = Student()  
            stu.name = raw_input("������ѧ����������")  
  
            #ƥ��ѧ��ID�Ƿ�����0--9�е�����  
            while True:  
                stu.ID = raw_input("������ѧ����ID:")  
                #��������һ��������ʽ��ģ��  
                p = re.compile( '^[0-9]{3}$' )  
                if p.match( stu.ID ):  
                    break  
                else:  
                    print "ѧ����ID���������ȷ��ʽӦ��Ϊ0--9֮�����λ����!"  
  
            #ƥ��ѧ���ķ����Ƿ�����0--100֮��  
            while True:      
                stu.score = eval( raw_input("������ѧ���ķ�����") )  
                #������ͨ�ķ������жϷ����Ƿ���ϱ�׼  
                #if stu.score >= 0 and stu.score <= 100:  
                #   break  
                #����������ʽ���жϷ����Ƿ���ϱ�׼  
                if re.match( "^[0-9]" ,str(stu.score) ) and stu.score<=100 and  stu.score >= 0 :  
                    break   
                else:  
                    print "����������ʵ�������Ӧ��Ϊ0--100֮�������!"  
  
            if Add( stulist , stu ) == 1:  
                print "ѧ����Ϣ���ӳɹ�!"  
            else:  
                print "ѧ����Ϣ����ʧ��!"  
        elif nChoose == "2":  
            QueryMenu( stulist )  
        elif nChoose == "3":  
            DeleteMenu( stulist )  
        elif nChoose == "4":  
            PrintAllStudentInfo( stulist )  
        elif nChoose == "5":  
            BuddleSortByScore( stulist )  
  
            print "Do you want to save the sorted result?"  
            choose = raw_input("please input your choice:Y/N:")  
            if choose == 'Y' or choose == 'y':  
               file_object = open("students.txt","w+")  
               for stu2 in stulist:  
                   file_object.write(stu2.ID)  
                   file_object.write(" ")  
                   file_object.write(stu2.name)  
                   file_object.write(" ")  
                   file_object.write(str(stu2.score))  
                   file_object.write("\r\n")  
        elif nChoose == "6":  
            return  
        else:  
            print "�����������������룡"   
              
#���Ժ�������  
if __name__ == '__main__':  
    #����һ���б������洢����ѧ������Ϣ  
    stulist = []  
      
    #��ʼ�������ļ��ж�ȡ��Ϣ  
    Init( stulist )  
      
    #�˵�����  
    menu( stulist )  