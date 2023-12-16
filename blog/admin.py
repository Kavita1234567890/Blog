from django.contrib import admin
from . models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date',)
    search_fields = ('title',)
    
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','url','cat',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 5
    
admin.site.register(Post,PostAdmin)    
