from django.shortcuts import render
from .models import Article
# Create your views here.

def index_view(request):
    articles = Article.objects.all()
    return render(request, "mainapp/index.html", {'articles': articles})
