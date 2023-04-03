from django import forms
import re
#lấy thư viện của user
from django.contrib.auth.models import User
#lỗi exception
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username=forms.CharField(label='Tài khoản', max_length=30)
    email=forms.EmailField(label='Email')
    password1=forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2=forms.CharField(label='Nhập lại Mật khẩu', widget=forms.PasswordInput())

    #nhập hàm này là password2 đã nhập rồi, kiểm tra xem cái 
    def clean_password2(self):
        #kiểm tra password1 có trong cái self.cleaned_data hay không
        if 'password1' in self.cleaned_data:
            password1=self.cleaned_data['password1']
            password2=self.cleaned_data['password2']
            #nếu password1==password2
            if password1==password2 and password1:
                return password2
        #nêu không sẽ nhập là Mật khẩu không hợp lệ
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    #kiểm tra user_name có điều gì đặc biệt không
    def clearn_username(self):
        username=self.cleaned_data['username']
        #kiểm tra xem có ký tự đặc biệt trong username thì trả về lỗi
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")

        try:
            User.objects.get(username=username)
        #trả về không có user nào tồn tại
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")
    #hàm save
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])