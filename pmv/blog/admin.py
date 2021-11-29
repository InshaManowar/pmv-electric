from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.






class BlogAdmin(SummernoteModelAdmin):
    list_display = ('author', 'publish_date', 'title')
    list_filter = ('title', 'author')
    prepopulated_fields={'slug':('title',)}
    summernote_fields =('snippet', 'content',)

    



admin.site.register(Blog, BlogAdmin)
