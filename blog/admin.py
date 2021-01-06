from django.contrib import admin
from .models import Post, Category,Comment 
# Register your models here.


admin.site.site_header="Blog Time"
admin.site.site_title = "Blog Time Site administration"
admin.site.index_title = "Dashboard"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','publish','status','category')
    list_filter=('status','created','publish','author')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=('status','-publish')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('post','name','email','content','timestamp')
    search_fields=('post','name','content','timestamp')

      

    