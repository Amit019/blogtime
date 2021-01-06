from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=250)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name  

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')         

class Post(models.Model):
    STATUS_CHOICES =(('draft','Draft'),('published','Published'),)
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)
    overview =models.TextField()
    content =RichTextUploadingField(null=True, blank=True)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updates=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')
    thumbnail = models.ImageField(upload_to='static/upload/img', default='None')
    read =models.IntegerField(default=10) 
    author  =models.ForeignKey(User,on_delete=models.CASCADE)
    objects=models.Manager()
    published=PublishedManager()
    tags=TaggableManager()
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    # @property    
    # def get_comments(self): 
    #     return self.comments.all() .order_by('-timestamp')  

class Comment(models.Model):
    post =models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=80,null=True,)
    email = models.EmailField(max_length=200, blank=True)
    reply=models.ForeignKey('self',null=True,related_name='replies',blank=True,on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)



