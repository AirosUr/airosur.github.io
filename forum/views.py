from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person

def index(request):
	people = Person.objects.all()
	return render(request, "forum.html", {"people": people})

def create(request):
	if request.method == "POST":
		mess = Person()
		mess.name = request.POST.get("name")
		mess.message = request.POST.get("message")
		mess.save()
	return HttpResponseRedirect("/forum")
		
def delete(request):
	person = Person.objects.all()
	person.delete()
	return HttpResponseRedirect("/forum")
	