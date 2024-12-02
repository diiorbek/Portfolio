from django.contrib import admin
from .models import ProjectModel, BlogModel, CommentModel, ContactModel, TestimonialModel

@admin.register(ProjectModel)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'url')
    search_fields = ('name', 'category')
    list_filter = ('category',)

@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'theme', 'created_date')
    search_fields = ('title', 'theme')
    list_filter = ('theme',)
    
@admin.register(CommentModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'blog', 'rating')
    search_fields = ('name', 'email')
    list_filter = ('rating',)
    
@admin.register(ContactModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    
@admin.register(TestimonialModel)
class ColleagueAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'start_date', 'rating') 
    list_filter = ('job_title', 'start_date')  
    search_fields = ('full_name', 'job_title', 'description')  
