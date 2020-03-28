from django.shortcuts import render

def index(request):
    return render(request, "javascript1.html")
	
def index2(request):
    return render(request, "javascript2.html")