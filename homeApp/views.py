from django.shortcuts import render
from .models import File
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'files': File.objects.all(),
    }
    return render(request, 'home/index.html', context=context)

@login_required
def upload(request):
    context = {
        
    }
    return render(request, 'home/upload.html', context=context)
