from django.contrib import admin
from .models import Category, ArtCat, Article, ArtParty
# Register your models here.

admin.site.register(Category)
admin.site.register(ArtCat)
admin.site.register(Article)
admin.site.register(ArtParty)