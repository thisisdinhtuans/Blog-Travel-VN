from django.test import TestCase
from .models import Post
# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        Post.objects.create(
            title='myTitle',
            body='just a Test'
        )

    def test_string_representation(self):
        #tạo 1 cái title khác
        post = Post(title='My entry title')
        #sẽ kiểm tra cái post nayfcos trả về dúng title hay ko
        self.assertEqual(str(post), post.title)

    def test_post_list_view(self):
        response = self.client.get('/blog/')
        #kiểm tra status_code=200 hay k
        self.assertEqual(response.status_code, 200)
        #kiểm tra xem là cái respone có chứa cái title này k, vì cái Post này trả về cái tiele
        self.assertContains(response, 'myTitle')
        #xem nó có sử dụng cái templates blog.html này hay không
        self.assertTemplateUsed(response, 'blog/blog.html')

    #xứ lý bài viết
    def test_post_detail_view(self):
        #kiểm tra cái id=1 xem nó như nào
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'myTitle')
        self.assertTemplateUsed(response, 'blog/post.html')