from django.contrib import admin
from .models import Post,Comment,BlogPost


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at','updated_at']
    
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'created_by', 'created_at']
admin.site.register(Comment, CommentAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at', 'updated_at']
admin.site.register(BlogPost,BlogPostAdmin)
