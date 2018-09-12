from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
import datetime
# Create your views here.
def inserter(request):
    return HttpResponse("<form name='xyz' action='./done' method='GET'>"
                        "<br><input type='text' name='title'><br>"
                        "<input type='text' name='body'><br>"
                        "<input type='submit' name='submit'>"
                        "</form> ")
def saver(request):
    if 'title' in request.GET and request.GET['title']:
        title=request.GET['title']
    if 'body' in request.GET and request.GET['body']:
        body=request.GET['body']

    blog=Post(title=title, body=body, date=datetime.datetime.now())
    blog.save()
    return HttpResponse("<h1>{{blog.title}}<h1>")

