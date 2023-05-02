from django.test import TestCase
from ..models import ArtCat, Article

# Create your tests here.

class TestArticle(TestCase):
    
    
    def setUp(self):
        '''
        Создаем товар для проверки
        '''
        artcat = ArtCat.objects.create(name='Подкатегория_1')
        code = '0001'
        name = 'Товар'
        is_active = True
        self.article = Article.objects.create(code=code, name=name, is_active=is_active, artcat=artcat)
    
    
    def tearDown(self):
        '''
        Удаляем товар
        '''
        Article.objects.get(id=self.article.pk).delete()
    
    
    def test_init_article(self):
        '''
        Проводим проверку init модкли Article
        '''
        self.assertEqual(self.article.name, 'Товар')
        
        
    def test_str_article(self):
        '''
        Проводим проверку str модкли Article
        '''
        self.assertEqual(str(self.article.name), 'Товар')
    
    
    def test_init_artcat(self):
        '''
        Проводим проверку init модели ArtCat
        '''
        self.assertEqual(self.article.artcat.name, 'Подкатегория_1')
        