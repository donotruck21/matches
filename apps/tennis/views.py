from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import User, Post, Message, Comment


# Create your views here.

def index(request):

	return render(request, 'tennis/index.html')
