from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.

def index(request):
	# return HttpResponse('HELLO FROM BLOGPOST!')

	posts = Posts.objects.all()[:10]

	content = {
		'body':'this is my inputted post beybe!',
		'posts' : posts
	}

	return render(request,'posts/index.html', content)

def details(request,id):
	post = Posts.objects.get(id=id)

	content = {
		'post' : post
	}

	return render(request,'posts/details.html', content)
