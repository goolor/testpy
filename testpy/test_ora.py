#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import cx_Oracle

conn = cx_Oracle.connect("icd/Hwcti123@132.37.10.18:1526/hwctidb")
conn.close()
