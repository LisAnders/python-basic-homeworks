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
    
    
    def test_status_code(self):
        '''
        Тест доступности страницы /article-list/
        '''
        response = self.client.get('/article-list/')
        self.assertEqual(response.status_code, 200)
        
        
    def test_context_data(self):
        '''
        Тест контекста страницы /article-list/
        '''
        response = self.client.get('/article-list/')
        self.assertEqual(response.context['object_list'].get().code, '0001')
        self.assertTrue('Товар', response.context)
        
        
    def test_content_data(self):
        '''
        Тест контента страницы
        '''
        button_create = '<a class="btn btn-sm btn-success" href="/article-create/">Создать</a>'
        response = self.client.get('/article-list/')
        self.assertIn(button_create, response.content.decode(encoding='utf-8'))
        