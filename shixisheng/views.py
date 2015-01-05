#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
import datetime
from django.template.response import TemplateResponse as TR
from shixisheng.models import student,Image
def home(request):
 	d = {"date":str(datetime.datetime.now())}
	all = student.objects.all()
	d['all'] = all
	
	all_img = Image.objects.all()
	d['all_img'] = all_img

	return TR(request,"index.html",d)
def hello(request,abcd):
	d = {"abc":abcd,"date":str(datetime.datetime.now())}
	all = student.objects.all()
	d['all'] = all
	return TR(request,"hello.html",d)
def new(request):
	s = student()
	s.name    = request.POST['name']
	s.address = request.POST['address']
	s.content = request.POST['content']
	s.count   = 0
	s.save()
	return redirect("/hello/wertth")


def delete(request,id):
	s = student.objects.get(id = int(id))
	s.delete()
	return redirect("/hello/fssdfg")
	
def edit_view(request,id):
	s = student.objects.get(id = int(id))
	time = datetime.datetime.now()
	d = {"s":s,"t":str(time)}
	return TR(request,"edit.html",d)

def edit(request,id):
	s = student.objects.get(id = int(id))
	s.name = request.POST['name']
	s.address = request.POST['address']
	s.save()
	return redirect("/hello/fdsdsfd")