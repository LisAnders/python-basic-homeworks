from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from .forms import ArticleForm


def index_view(request):
    return render(request, "mainapp/index.html")


class ArticleList(ListView):
    model = Article
    

class ArticleDetail(DetailView):
    model = Article


class ArticleCreate(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = "/article-list/"
    

class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = "/article-list/"


class ArticleDelete(DeleteView):
    model = Article
    success_url = "/article-list/"