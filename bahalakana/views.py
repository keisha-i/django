from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')
def blog(request):
    return render(request, 'pages/blog.html')
def contact(request):
    return render(request, 'pages/contact.html')