# Create your views here.
#coding=utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout

def index(request):
	username='david_learn_web'
	return render(request,'accounts/index.html',{'username':username})

def register(request):
	'''注册视图'''
	if request.method=='POST':
		#注册完毕 直接登录
		return HttpResponseRedirect('/accounts/index')
	return render(request,'accounts/register.html',)

def login(request):
	'''登录视图'''
	template_var={}
	if request.method=='POST':
		username=request.POST.get('username')
		template_var={'eeror':'must first register','username':username}
	return render(request,'accounts/login.html',template_var,)

def logout(request):
	return render(request,'accounts/logout.html',)
