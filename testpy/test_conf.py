#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import configparser
import cx_Oracle

ConfFile='./conf.ini'

#config1 = configparser.ConfigParser()
config1=configparser.ConfigParser(inline_comment_prefixes=(';','#'))
config1.read(ConfFile)
#for section in config1.sections():
#	print("'["+section+"]'")
#	for key in config1[section]:
#		print('{0} = {1}'.format(repr(key),repr(config1[section][key])))
#
conn1_ora_str=config1['Oracle']['user']+'/'+config1['Oracle']['password']+'@'+config1['Oracle']['addr']+':'+config1['Oracle']['port']+'/'+config1['Oracle']['sid']
#Get the Oracle connect string

conn1_ora = cx_Oracle.connect(conn1_ora_str)
cursor1 = conn1_ora.cursor()

cursor1.execute("SELECT * FROM User_Tables")
#line2=cursor1.fetchone()
#print(len(line2))
print('')
logfile1=open('./log_oracle.txt', 'w')

for row1 in cursor1: 
#	print("Row:",row1)
	logfile1.write(str(eval(str(row1))))
	#logfile1.write(str(row1))
	logfile1.write("\n")
print(cursor1.rowcount)
logfile1.close()
#Now to close the cursor and Oracle connections
cursor1.close()
conn1_ora.close()


