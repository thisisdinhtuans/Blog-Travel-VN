from django.urls import path
from . import views
#đây là views có cái hàm nó đã viết sẵn và nó trùng với cái views ở trên và đặt nó là auth_views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index),
   path('contact/', views.contact, name='contact'),
   path('register/', views.register, name="register"),
   path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
   #khi logout thì nó về trang chủ, chính là cái'/'
   path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
]

