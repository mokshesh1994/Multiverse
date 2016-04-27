from django.shortcuts import render
from .models import story_document

# Create your views here.

def home(request):
	story = story_document.objects.all()
	return render(request, 'multiverse/home.html',{'story':story})


