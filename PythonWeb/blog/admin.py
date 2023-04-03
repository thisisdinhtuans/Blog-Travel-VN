from django.contrib import admin
from .models import Post, Comment
# Register your models here.
#cho kế thừa admin.StackedInline
class CommentInline(admin.StackedInline):
    #đưa model gắn vào comment
    model=Comment
class PostAdmin(admin.ModelAdmin):
    list_display= ['title', 'date']
    list_filter=['date']
    search_fields=['id']
    #thêm thuộc tính inline 
    inlines=[CommentInline]
admin.site.register(Post, PostAdmin)
