from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

def detail(request, question_id):
    return HttpResponse("Detail %s" % question_id)

def vote(request, question_id):
    return HttpResponse("voting on question %s" % question_id)
