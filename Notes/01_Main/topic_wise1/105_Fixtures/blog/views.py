from django.shortcuts import render
from .models import BlogPost

# Create your views here.


def home(request):
    context = {
        'post': BlogPost.objects.all()
    }
    return render(request, 'home.html', context)
