from django import forms
#tạo input của phần comment
from .models import Comment
#cho nó kế thừa cái ModelForm
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    #đây là hàm viết sẵn, mình phải override nó lại để thêm thà tác giả bài viết vào phần comment
    #thêm thuộc tình commit=true
    def save(self, commit=True):
        #commit=False để nó ko lưu vào database
        comment = super().save(commit=False)
        #hướng đối tượng
        comment.author = self.author
        comment.post = self.post
        #lưu lại vào databas, giờ mới lưu
        comment.save()
    #tạo class Meta để thể hiện cái comment forms này
    #tạo ra cái input để nó thực hiện cái Comment chỉ có trường body thôi
    class Meta:
        #nó cho ta tạo 4 cái input của phần models.py, nhưng mình chỉ cần tạo input của thà body thôi, còn 3 cái kia trong quá trình bình luận nó tự gán vào
        model = Comment
        fields = ["body"]
