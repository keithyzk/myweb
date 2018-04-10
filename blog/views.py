# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models

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
    return HttpResponseRedirect('/index/blog/')
 