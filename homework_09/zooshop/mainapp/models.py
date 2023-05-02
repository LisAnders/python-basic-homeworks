from django.db import models

# Create your models here.
# Категории
# Категории товаров
# Товары
# Партии товаров

class Category(models.Model):
    name = models.CharField(unique=True, max_length=50)
    
    def __str__(self) -> str:
        return self.name


class ArtCat(models.Model):
    name = models.CharField(unique=True, max_length=50)
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.name    
    

class Article(models.Model):
    code = models.CharField(unique=True, max_length=20)
    name = models.CharField(unique=False, max_length=50)
    is_active = models.BooleanField(default=True)
    artcat = models.ForeignKey(ArtCat, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name  


class ArtParty(models.Model):
    party_number = models.CharField(unique=True, max_length=20)
    quantity = models.FloatField(null=False, default=0)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.party_number 
