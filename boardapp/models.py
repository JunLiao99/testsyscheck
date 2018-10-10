from django.db import models
import pyodbc
class BoardUnit(models.Model):
    bname = models.CharField(max_length=20, null=False)
    bgender = models.CharField(max_length=2, default='m', null=False)
    bsubject = models.CharField(max_length=100, null=False)
    btime = models.DateTimeField(auto_now=True)
    bmail = models.EmailField(max_length=100, blank=True, default='')
    bweb = models.CharField(max_length=200, blank=True, default='')
    bcontent = models.TextField(null=False)
    bresponse = models.TextField(blank=True, default='')
    
    def __str__(self):
        return self.bsubject

class history(models.Model):
    xactno = models.CharField(max_length=200, null=False)
    pltno = models.CharField(max_length=100, default='m', null=False)
    car_tp = models.CharField(max_length=100, null=False)
    vil_dt = models.CharField(max_length=100, null=False)
    vil_tm = models.EmailField(max_length=100, blank=True, default='')
    vil_add = models.CharField(max_length=200, blank=True, default='')
    rule_1 = models.TextField(null=False)
    vildatetime = models.DateTimeField(auto_now=True)
    vilinf = models.TextField(blank=True, default='')
    situa = models.TextField(blank=True, default='')
    piclink = models.TextField(blank=True, default='')
    expop = models.CharField(max_length=200, null=False)
    leader = models.CharField(max_length=100, default='m', null=False)


class caselist(models.Model):
    xactno = models.CharField(max_length=200, null=False)
    pltno = models.CharField(max_length=100, default='m', null=False)
    car_tp = models.CharField(max_length=100, null=False)
    vil_dt = models.CharField(max_length=100, null=False)
    vil_tm = models.EmailField(max_length=100, blank=True, default='')
    vil_add = models.CharField(max_length=200, blank=True, default='')
    rule_1 = models.TextField(null=False)
    vildatetime = models.DateTimeField(auto_now=True)
    vilinf = models.TextField(blank=True, default='')
    situa = models.TextField(blank=True, default='')
    piclink = models.TextField(blank=True, default='')
    # def __str__(self):
    #     return self.caseNAME



class check:
    def checkuser(self,name):
        print(name)
        cnxn = pyodbc.connect(r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=testDB;UID=sa;PWD=80689233;')
        cursor = cnxn.cursor()
        cursor.execute("select * from　auth_user where username = '"+name+"'")
        # cursor.execute("select * from　auth_user where name = %s",(name,))
        datas = cursor.fetchone()
        print(datas)
        return datas

    def listall(self):
        cnxn = pyodbc.connect(r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=testDB;UID=sa;PWD=80689233;')
        cursor = cnxn.cursor()
        cursor.execute("select * from　case_n")
        # cursor.execute("select * from　auth_user where name = %s",(name,))
        datas = cursor.fetchall()
        print(datas)
        return datas

    def CNname(self,user):
        cnxn = pyodbc.connect(r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=testDB;UID=sa;PWD=80689233;')
        cursor = cnxn.cursor()
        cursor.execute("select last_name from　auth_user where username = '"+user+"'")
        # cursor.execute("select * from　auth_user where name = %s",(name,))
        datas = cursor.fetchone()
        # print(datas)
        return datas

    def leader(self,user):
        cnxn = pyodbc.connect(r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=testDB;UID=sa;PWD=80689233;')
        cursor = cnxn.cursor()
        cursor.execute("select leader from　auth_user where username = '"+user+"'")
        datas = cursor.fetchone()
        return datas

    def expop(self,user):
        cnxn = pyodbc.connect(r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=testDB;UID=sa;PWD=80689233;')
        cursor = cnxn.cursor()
        cursor.execute("select exp_op from　auth_user where username = '"+user+"'")
        datas = cursor.fetchone()
        return datas

    
    def insert(self,id):
        cnxn = pyodbc.connect(r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=testDB;UID=sa;PWD=80689233;')
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO boardapp_history (id, xactno, pltno, car_tp, vil_dt, vil_tm, vil_add, rule_1, vildatetime, vilinf, situa, piclink) SELECT id, xactno, pltno, car_tp, vil_dt, vil_tm, vil_add, rule_1, vildatetime, vilinf, situa, piclink FROM boardapp_caselist WHERE id = '"+id+"'" )
        cnxn.commit()

    def insertexpop(self,id,expop):
        cnxn = pyodbc.connect(r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=testDB;UID=sa;PWD=80689233;')
        cursor = cnxn.cursor()
        cursor.execute("UPDATE boardapp_history set situa='"+expop+"' where id = '"+id+"'" )
        cnxn.commit()
        # datas = cursor.fetchone()
        # return datas
    # def delete(self,idd):

    #     cnxn = pyodbc.connect(r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=testDB;UID=sa;PWD=80689233;')
    #     cursor = cnxn.cursor()
    #     cursor.execute("delete from boardapp_caselist where id = '"+idd+"'")

import time
import traceback


