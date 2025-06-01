from django.contrib import admin
from .models import Post,Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at','updated_at']
    
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'created_by', 'created_at']
admin.site.register(Comment, CommentAdmin)
    