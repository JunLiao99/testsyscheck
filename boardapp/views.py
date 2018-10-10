# encoding:utf-8
from django.shortcuts import render, redirect
from boardapp import models, forms
from django.contrib.auth import authenticate
from django.contrib import auth
import math
from django.http import HttpResponse
from . import models
from .models import check
import datetime

check = models.check()

page = 0  #目前頁面,0為第1頁

def index(request, pageindex=None):  #首頁
	name = request.session['name']
	CNname = request.session['CNname']
	global page  #重複開啟本網頁時需保留 page1 的值
	pagesize = 3  #每頁顯示的資料筆數
	boardall = models.BoardUnit.objects.all().order_by('-id')  #讀取資料表,依時間遞減排序
	datasize = len(boardall)  #資料筆數
	totpage = math.ceil(datasize / pagesize)  #總頁數
	if pageindex==None:  #無參數
		page = 0
		boardunits = models.BoardUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='prev':  #上一頁
		start = (page-1)*pagesize  #該頁第1筆資料
		if start >= 0:  #有前頁資料就顯示
			boardunits = models.BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
			page -= 1
	elif pageindex=='next':  #下一頁
		start = (page+1)*pagesize  #該頁第1筆資料
		if start < datasize:  #有下頁資料就顯示
			boardunits = models.BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
			page += 1
	currentpage = page + 1  #將目頁前頁面以區域變數傳回html
	return render(request, "index.html", locals())

# def post(request):  #新增留言
# 	if request.method == "POST":  #如果是以POST方式才處理
# 		postform = forms.PostForm(request.POST)  #建立forms物件
# 		if postform.is_valid():  #通過forms驗證
# 		  subject = postform.cleaned_data['boardsubject']  #取得輸入資料
# 		  name =  postform.cleaned_data['boardname']
# 		  boo =  postform.cleaned_data['boardgender']
# 		  if boo == True: gender = 'm'
# 		  else: gender = 'f'
# 		  mail = postform.cleaned_data['boardmail']
# 		  web =  postform.cleaned_data['boardweb']
# 		  content =  postform.cleaned_data['boardcontent']
# 		  unit = models.BoardUnit.objects.create(bname=name, bgender=gender, bsubject=subject, bmail=mail, bweb=web, bcontent=content, bresponse='')  #新增資料記錄
# 		  unit.save()  #寫入資料庫
# 		  message = '已儲存...'
# 		  postform = forms.PostForm()
# 		  return redirect('/index/')	
# 		else:
# 		  message = '驗證碼錯誤！'	
# 	else:
# 		message = '標題、姓名、內容及驗證碼必須輸入！'
# 		postform = forms.PostForm()
# 	return render(request, "post.html", locals())

def login(request):  #登入
	# word = check.checkuser()
	# print(word)
	messages = ''  #初始時清除訊息
	if request.method == 'POST':  #如果是以POST方式才處理
		name = request.POST['username'].strip()  #取得輸入帳號
		password = request.POST['passwd']  #取得輸入密碼
		user1 = authenticate(username=name, password=password)  #驗證
		if user1 is not None:  #驗證通過
			if user1.is_active:  #帳號有效
				auth.login(request, user1)  #登入
				word = check.checkuser(name)
				request.session['name'] = name

				pname = request.session['name']
				CNname = word[6]
				request.session['CNname'] = CNname

				leader = check.leader(name)
				request.session['leader'] = leader[0]

				expop = check.expop(name)
				request.session['expop'] = expop[0]
				
				# print(CNname,'sss')
				return redirect('/index/')  #開啟管理頁面
			else:  #帳號無效
				message = '帳號尚未啟用！'
		else:  #驗證未通過
			message = '登入失敗！'
	return render(request, "login.html", locals())

def logout(request):  #登出
	auth.logout(request)
	return redirect('/index/')

def change(request): #管理新增資料
	messages =  models.caselist.objects.all().order_by('-id')  #获取全部数据
	# messages =  models.caselist.objects.filter(situa='未處理').order_by('-id')  #获取全部数据
	limit = 5
	paginator = Paginator(messages, limit)  #按每页10条分页
	page = request.GET.get('page','1')  #默认跳转到第一页

	result = paginator.page(page)

	name = request.session['name']
	CNname = request.session['CNname']
	leader = request.session['leader']
	expop = request.session['expop']

	return render(request, "change.html", {'messages' : result,'name': name,'leader': leader,'CNname': CNname,'expop': expop},locals())

# def serch(request): #管理新增資料
# 	return render(request, "serch.html", locals())

def adminmain(request, pageindex=None):  #管理頁面
	global page
	pagesize = 3
	boardall = models.BoardUnit.objects.all().order_by('-id')
	datasize = len(boardall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page =0
		boardunits = models.BoardUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='prev':
		start = (page-1)*pagesize
		if start >= 0:
			boardunits = models.BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
			page -= 1
	elif pageindex=='next':
		start = (page+1)*pagesize
		if start < datasize:
			boardunits = models.BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
			page += 1
	elif pageindex=='ret':  #按確定修改鈕後返回
		start = page*pagesize
		boardunits = models.BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
	else:  #按確定修改鈕會以pageindex傳入資料id
		unit = models.BoardUnit.objects.get(id=pageindex)  #取得要修改的資料記錄
		unit.bsubject=request.POST.get('boardsubject', '')
		unit.bcontent=request.POST.get('boardcontent', '')
		unit.bresponse=request.POST.get('boardresponse', '')
		unit.save()  #寫入資料庫
		return redirect('/adminmain/ret/')  #返回管理頁面,參數為ret
	currentpage = page+1
	return render(request, "adminmain.html", locals())

def delete(request, boardid=None, deletetype=None):  #刪除資料
	unit = models.BoardUnit.objects.get(id=boardid)  #讀取指定資料
	if deletetype == 'del':  #按確定刪除鈕
		unit.delete()
		return redirect('/adminmain/')
	return render(request, "delete.html", locals())


from django.db.models import Count,Sum
#只需修改index函数即可
from django.core.paginator import Paginator

# def serch(request):
# 	messages =  models.caselist.objects.all().order_by('-id')  #获取全部数据
# 	limit = 1
# 	paginator = Paginator(messages, 3)  #按每页10条分页
# 	page = request.GET.get('page','1')  #默认跳转到第一页

# 	result = paginator.page(page) 

# 	return render(request, 'change.html', {'messages' : result})




def serch(request):
	messages =  models.caselist.objects.all().order_by('-id')  #获取全部数据
	# limit = 3
	# paginator = Paginator(messages, limit)  #按每页10条分页
	# page = request.GET.get('page','1')  #默认跳转到第一页

	# result = paginator.page(page) 
# 每页post数量
	limit = 5
	messages = models.caselist.objects.all()
	paginator = Paginator(messages, 3)
	page = request.GET.get('page','1')
	try:
		messages = paginator.page(page)
	except PageNotFound:
		messages = paginator.page(1)
	except EmptyPage:
		messages = paginator.page(paginator.num_pages)
	# result = paginator.page(page)
	return render(request, 'change.html', context={'messages' : messages})

import sys
import codecs
import json
from collections import OrderedDict
def getjsonq(request):

	q=request.POST['data1']
	leader = request.session['leader']
	exp_op = request.session['expop']
	exp_dt=datetime.datetime.now().strftime('%Y%m%d')
	exp_dt=str(int(exp_dt)-19110000)
	exp_tm=datetime.datetime.now().strftime('%H%M%S')

	vilcnt = 35
	piccnt = 35
	# json.dumps(q)
	# q=(q.dict())
	# q = json.dumps(q, sort_keys=True, indent=4, separators=(',', ':'),ensure_ascii=False)
	# del q['csrfmiddlewaretoken']
	# q = q['data1']
	# q = q[1:-1]
	result = json.loads(q)
	print(result)

	d = {"leader": leader, "exp_dt": exp_dt, "exp_tm": exp_tm, "exp_op": exp_op,
		"vilcnt": vilcnt, "piccnt": piccnt, "vilrec":result}
	# q = q.replace("\\" , "")
	# q = q.strip(' "[]" ')	
	# print(q,type(q))
	# q = json.dumps(q, ensure_ascii=False, indent=4, sort_keys=True) + ','
	# print(json_data)
	# store(json_data)
	filename = leader+'_'+exp_dt+exp_tm+'_'+exp_op+'.json'
	print(filename)

	js = json.dumps(d, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
	fp = codecs.open(filename, 'a+', 'utf-8')
	fp.write(js)
	fp.close()

def getjsonid(request):
	q=request.POST['data2']
	q=q[1:-1]
	q=q.replace('"','')
	input1_list=q.split(",")
	print(input1_list,type(input1_list))
	for i in input1_list:
		case = models.caselist.objects.get(id=i)
		case.delete()
	# return render(request, 'change.html', context={'messages' : messages})
