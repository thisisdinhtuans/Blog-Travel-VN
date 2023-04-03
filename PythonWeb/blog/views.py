from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.
def list(request):
   Data = {'Posts': Post.objects.all().order_by('-date')}
   return render(request, 'blog/blog.html', Data)

#kế thừa ListView
class PostListView(ListView):
   queryset=Post.objects.all().order_by('-date')
   template_name='blog/blog.html'
   context_object_name='Posts'
   #mỗi trang chỉ chưa 10 bài viết
   paginate_by: int=10
class PostDetailView(DetailView):
   model=Post
   template_name='blog/post.html'
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
# Create your views here.

def post(request, pk):
   #lấy từ bài viết Post có khóa ngoại là cái pk này, nếu ko có trả về lỗi 404
   post = get_object_or_404(Post, pk=pk)
   #khởi tạo thì nó vào CommentForm() ở forms.py<blog>, khi chưa truyền vào thì 2 thà đó trả về là NONE<hàm__init__>
   form = CommentForm()
   #
   if request.method == 'POST':
      #đưa tác giả bài viết vào form
      form = CommentForm(request.POST, author=request.user, post=post)

      if form.is_valid():
         #nếu hợp lệ thì lưu, tức là chạy hàm save ở forms.py<blog>
         form.save()
         return HttpResponseRedirect(request.path)
   return render(request, "blog/post.html", {"post": post, "form": form})
