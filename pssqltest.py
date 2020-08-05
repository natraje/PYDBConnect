'''
Created on Dec 23, 2019

@author: natra
'''
import psycopg2 as psy

conn=psy.connect(host="localhost",database="MLAI", user="postgres", password="secret")
cur=conn.cursor()

cur.execute('select * from account')
print(cur)
allrows=cur.fetchall();
print(allrows[:5])