from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "base/index.html")

def about(request):
    return render(request, "base/about.html")

def category(request):
    return render(request, "base/category.html")

def myskills(request):
    return render(request, "base/myskills.html")