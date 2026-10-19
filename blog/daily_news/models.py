from django.db import models


# Create your models here.
class Blog(models.Model):
    headline = models.CharField()
    body = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    published_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.headline
