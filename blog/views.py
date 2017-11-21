# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse

from .models import Article, Comments


class HomeView(generic.ListView):
    template_name = "blog/home.html"
    context_object_name = 'latest_blog_list'
    def get_queryset(self):
        return Article.objects.order_by('-posted_date')[:3]
    
class ArticleView(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'
    
class ArchiveView(generic.ListView):
    template_name = "blog/archive.html"
    context_object_name = 'full_blog_list'
    def get_queryset(self):
        return Article.objects.order_by('-posted_date')

def postComment(request, blog_id):
    c = Comments()
    
    c.commenters_nickname = request.POST.commenters_nickname
    c.content = request.POST.content
    c.email_address = request.POST.email_address
    
    b= Article.objects.get(id=blog_id)
    c.blog = b
    c.save()
    
    return HttpResponseRedirect(reverse('blog:comments', args=(b)))