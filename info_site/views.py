from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'info_site/index.html', context)

def about(request):
    context = {}
    return render(request, 'info_site/about.html', context)

def downloads(request):
    context = {}
    return render(request, 'info_site/downloads.html', context)
