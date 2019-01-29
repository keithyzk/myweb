# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models
# from .models import *

# def index(request):
#     return render(request,'index.html')

def blog(request):
    ariticles = models.Ariticle.objects.all()
    return render(request,'blog.html',{'ariticles' :ariticles})

def ariticle_page(request, ariticle_id):
    ariticle = models.Ariticle.objects.get(pk=ariticle_id)
    return render(request, 'ariticle_page.html',{'ariticle' : ariticle})

def edit_page(request, ariticle_id):
    if str(ariticle_id) == '0':
        return render(request, 'edit_page.html')
    ariticle = models.Ariticle.objects.get(pk=ariticle_id)
    return render(request, 'edit_page.html', {'ariticle' : ariticle})

def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    ariticle_id = request.POST.get('ariticle_id', '0')
    if ariticle_id == '0':
        models.Ariticle.objects.create(title=title, content=content)
        ariticles = models.Ariticle.objects.all()
        return HttpResponseRedirect('/index/blog/')
    ariticle = models.Ariticle.objects.get(pk=ariticle_id)
    ariticle.title = title
    ariticle.content = content
    ariticle.save()
    return HttpResponseRedirect('/blog/index/')


def addSQLdb(request):
    ip = request.POST.get('ip', 'IP')
    mysqltype = request.POST.get('mysqltype', 'MYSQLTYPE')
    username = request.POST.get('username', 'USERNAME')
    password = request.POST.get('password', 'PASSWORD')
    port = request.POST.get('port', 'PORT')
    master_ip = request.POST.get('master_ip', 'MASTER_IP')
    master_port = request.POST.get('master_port', 'MASTER_PORT')
    # dbList_id = request.POST.get(dbID, '0')
    mysql_list = models.mysql_list.objects.get(pk=1)
    mysql_list.ip = ip
    mysql_list.mysqltype = mysqltype
    mysql_list.username = username
    mysql_list.password = password
    mysql_list.port = port
    mysql_list.master_ip = master_ip
    mysql_list.master_port = master_port
    mysql_list.save()
    return HttpResponseRedirect('/blog/index/')



