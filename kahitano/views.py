from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')
def book(request):
    return render(request, 'pages/book.html')
def about(request):
    return render(request, 'pages/about.html')