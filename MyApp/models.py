from django.db import models

class ProjectModel(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="Projects/")
    
    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"

    def __str__(self):
        return f"{self.name} - {self.category}"
    
class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(upload_to="Blogs")
    
    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"
        
    def __str__(self):
        return f"{self.title} - {self.theme}"

class CommentModel(models.Model):
    blog = models.ForeignKey(BlogModel, related_name='comments', on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment_text = models.TextField()
    rating = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}"
    
class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Yangi habar: {self.name} ({self.email})"
    
class TestimonialModel(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Full name")
    job_title = models.CharField(max_length=100, verbose_name="Work")
    start_date = models.DateField(verbose_name="Date")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, verbose_name="Rating",
        help_text="from 0 to 5"
    )
    image = models.ImageField(upload_to="Testimonials")

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"


    def __str__(self):
        return f"{self.full_name} - {self.job_title}"