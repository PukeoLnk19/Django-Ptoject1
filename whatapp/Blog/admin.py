from django.contrib import admin
from .models import Blog,Blogs

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','date','update','show_profile_pic' ]
    search_fields = ['title']
    list_filter = ['title']


class BlogsAdmin(admin.ModelAdmin):
    list_display = ['title','date','update','show_profile_pic' ]
    search_fields = ['title']
    list_filter = ['title']


# Register your models here.

admin.site.register(Blog, BlogAdmin)
admin.site.register(Blogs, BlogsAdmin)

