from django.contrib import admin
from .models import BlogPost,Comments,Tag
# Register your models here.


admin.site.register(BlogPost)
admin.site.register(Comments)
admin.site.register(Tag)