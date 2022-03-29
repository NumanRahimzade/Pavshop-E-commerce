import email
from turtle import title
from django.test import TestCase
from blog.models import Blog, Category, User, Tag


class TestBlog(TestCase):
    # print(Category.objects.first().name)
    def setUp(self):
        cat = Category.objects.create(name='Caat1')
        tag = Tag.objects.create(title='tag')
        user = User.objects.create_user(username='idris', email='idris@gmail.com', password='sdfnsdjfnsjdf')
        self.data1 = {
            'category' : cat,
            'author' : user,
            'title' : 'hey',
            'description' : 'how is life going on?'
        }


        self.blog1 = Blog.objects.create(**self.data1)
        self.blog1.tags.add(tag)


    def test_blog_data(self):
        self.assertEqual(self.data1['description'], self.blog1.description)