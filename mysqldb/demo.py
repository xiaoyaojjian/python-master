# -*- coding: utf-8 -*-       
#mysqldb      
import time, MySQLdb      
     
#连接      
conn=MySQLdb.connect(host="localhost",user="root",passwd="root",db="test",charset="utf8")    
cursor = conn.cursor()     ##建立游标 
  
#删除表  
sql = "drop table if exists user"  
cursor.execute(sql)  
  
#创建  
sql = "create table if not exists user(name varchar(128) primary key, created int(10))"  
cursor.execute(sql)  
  
#写入      
sql = "insert into user(name,created) values(%s,%s)"     
param = ("aaa",int(time.time()))      
n = cursor.execute(sql,param)      
print 'insert',n      
     
#写入多行      
sql = "insert into user(name,created) values(%s,%s)"     
param = (("bbb",int(time.time())), ("ccc",33), ("ddd",44) )  
n = cursor.executemany(sql,param)      
print 'insertmany',n      
  
#更新      
sql = "update user set name=%s where name='aaa'"     
param = ("zzz")      
n = cursor.execute(sql,param)      
print 'update',n      
     
#查询      
n = cursor.execute("select * from user")      
for row in cursor.fetchall():      
    print row  
    for r in row:      
        print r      
     
#删除      
sql = "delete from user where name=%s"     
param =("bbb")      
n = cursor.execute(sql,param)      
print 'delete',n      
  
#查询      
n = cursor.execute("select * from user")      
print cursor.fetchall()      
  
cursor.close()      
     
#提交      
conn.commit()  
#关闭      
conn.close()   









"""
查询语句数据结构优化
""" 
#coding:utf-8
import time, MySQLdb
#连接      
conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="daSDSAkMNDSNKA1231",db="reboot",charset="utf8")
cursor = conn.cursor()     ##简历游标 
"""
n = cursor.execute("select * from idc")
ret = cursor.fetchall()
"""
fields = ['idc_name','phone','email']
n = cursor.execute("select idc_name,phone,email from idc")
result_set = cursor.fetchone()
result = dict([(k, result_set[i]) for i,k in enumerate(fields)])
print result
cursor.close()
#提交      
conn.commit()
#关闭      
conn.close()
~                  
###查询单行的时候,结果:
"""
(env)[root@BJ-monitor-h-01 python]# python mysql_dbtest.py 
{'phone': u'18874374260', 'idc_name': u'\u4e92\u8054\u6e2f\u6e7e', 'email': u'123@123.com'}
"""

"""
查询多行时候
"""
#coding:utf-8
import time, MySQLdb
#连接      
conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="daSDSAkMNDSNKA1231",db="reboot",charset="utf8")
cursor = conn.cursor()     ##简历游标 
"""
n = cursor.execute("select * from idc")
ret = cursor.fetchall()
"""
fields = ['idc_name','phone','email']
n = cursor.execute("select idc_name,phone,email from idc")
result_set = cursor.fetchall()
result = [dict((k, row[i]) for i,k in enumerate(fields)) for row in result_set]
print result
cursor.close()
#提交      
conn.commit()
#关闭      
conn.close()
~                                                                                                                                   
~                      
