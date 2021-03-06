from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
# Create your views here.


# posts = [
#     {
#         'author': 'Corey MS',
#         'title' : 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 15, 2021'
#     },
#     {
#         'author': 'Jane Doe',
#         'title' : 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 16, 2021'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
