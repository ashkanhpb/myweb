from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'status' , 'published_date' , 'slug']
    list_display = ('title', 'published_date', 'status')
    search_fields = ('title', 'content')
    list_filter = ('status',)
    prepopulated_fields = {"slug": ["title"]}

admin.site.register(Post, PostAdmin)