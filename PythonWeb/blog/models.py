from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)
    
    def __str__(self):
        return self.title
from django.conf import settings

class Comment(models.Model):
    #mình sẽ đặt khóa ngoại
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    #khi xóa bài viết sẽ xóa cả bình luận
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #nội dung bình luận thì mình viết bằng text
    body = models.TextField()
    #thể hiện ngày bình luận
    date = models.DateTimeField(auto_now_add=True)
