from django.db import models

# Create your models here.

class Homepage(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200)
    
class ContactMe(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    subject = models.TextField()
    user_message = models.TextField()

    class Meta:
        verbose_name_plural = "Contact Me"
    
    def __str__(self) -> str:
        return self.user_name + " : " + self.subject