from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


from django.utils.text import slugify


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image  = models.ImageField(upload_to='profile/',null=True,blank=True)
    # name = models.CharField(max_length=50)
    work = models.CharField(max_length=50,default='developer')
    # email = models.EmailField(max_length=100)
    total_palylist = models.IntegerField(default=0)
    total_videos = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)
    total_comments = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, null=True)
    



    def save(self,*args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Author,self).save(*args, **kwargs)

    

    def __str__(self):
        return str(self.user)




# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Author.objects.create(user=instance)