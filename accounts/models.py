from django.db import models
from django.utils.text import slugify



def generate_unique_slug(instance, value):
    base_slug = slugify(value)
    
    if not base_slug:
        base_slug = instance._meta.model_name
    slug = base_slug
    counter = 1
    
    queryset = instance.__class__.objects.all()
    
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)
        
    while queryset.filter(slug=slug).exists():
        slug = f'{base_slug}-{counter}'
        counter+=1
        
    return slug

# Create your models here.
    
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.ImageField(upload_to='course/thumbnail/', null=True, blank=True)
    course_file = models.FileField(upload_to='course/files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    


