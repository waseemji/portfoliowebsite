from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=25)

    def __str__(self):
        return self.caption


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="images")
    description = models.TextField(max_length=500)
    slug = models.SlugField(default="", blank=True ,db_index=True)
    tag = models.ManyToManyField(Tag)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comments(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_comment = models.TextField(max_length=550)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return "Comment for post ' " + self.post.title +" ' "

