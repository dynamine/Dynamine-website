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

def walkthrough(request):
	context = {}
	return render(request, 'info_site/walkthrough.html', context)

def walkthrough_install(request):
	context = {}
	return render(request, 'info_site/walkthrough_install.html', context)

def walkthrough_add_coin(request):
	context = {}
	return render(request, 'info_site/walkthrough_add_coin.html', context)

def walkthrough_add_coin_1(request):
	context = {}
	return render(request, 'info_site/walkthrough_add_coin_1.html', context)

def walkthrough_add_coin_2(request):
	context = {}
	return render(request, 'info_site/walkthrough_add_coin_2.html', context)

def walkthrough_end(request):
	context = {}
	return render(request, 'info_site/walkthrough_end.html', context)