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

        # with connection.cursor() as cursor:
        #     cursor.execute("select * from products")
        #     datas = cursor.fetchall()
        # return datas
import time
import traceback


