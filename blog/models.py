from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True , allow_unicode=True , null=True)
    def __str__(self):
        return self.title + ' - ' + self.content
    class Meta:
        ordering = ['-created_date']
    #def get_absolute_url(self):
     #    return reverse("article_detail", kwargs={"slug": self.slug})