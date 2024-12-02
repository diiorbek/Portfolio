from django.shortcuts import render, redirect, get_object_or_404
from .models import ProjectModel, BlogModel, CommentModel, ContactModel, TestimonialModel
from .forms import CommentForm, ContactForm
from django.http import JsonResponse


def main(request):
            
       
    projects = ProjectModel.objects.all()
    blogs = BlogModel.objects.all()
    contacts = ContactModel.objects.all()
    testimonials = TestimonialModel.objects.all()
    
    return render(request, 'index.html', {'projects': projects, 'blogs': blogs, 'testimonials': testimonials, 'contacts': contacts})

def blog_detail(request, blog_id):
    blog = BlogModel.objects.get(pk=blog_id)
    comments = CommentModel.objects.filter(blog=blog).order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blog = blog  
            new_comment.save()
            return redirect('blog_detail', blog_id=blog_id) 
    else:
        form = CommentForm()
    
    return render(request, 'blog_detail.html', {'blog': blog, 'comments': comments, 'form': form})