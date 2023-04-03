from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
   return render(request, 'pages/home.html')

def contact(request):
    return render(request, 'pages/contact.html')

def register(request):
   form=RegistrationForm()
   #nếu method =POST thì mình gọi dữ diệu thừ cái form
   if request.method == 'POST':
      #đưa dữ liệu người dùng vào cái form này
      form=RegistrationForm(request.POST)
      #kiểm tra xem có hợp lệ không, ở mục forms.py<home> thì nó hợp lệ thì được, cái forms hợp lệ sẽ là tự động của nó
      if form.is_valid():
         #gọi hàm save để tạo tài khoản ở mục forms.py<home>
         form.save()
         #nếu thành công thì cho nó quay lại trang chủ, đẫn đến cái đường dẫn trang chủ
         return HttpResponseRedirect('/')
   #đến cái đường dẫn và đưa cái form vào 
   return render(request, 'pages/register.html',{'form': form})