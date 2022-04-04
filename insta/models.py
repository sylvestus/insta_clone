from email.mime import image
from unicodedata import name
from django.contrib.auth.models import User
from django.db import models
import datetime as dt
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    profilePhoto = models.ImageField(upload_to = 'media/',default="") 
    bio = models.TextField()
    

    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()
        
    @classmethod
    def get_profile(cls,id):
        profile = Profile.objects.all()
        return profile
        
    @classmethod
    def update_profile(cls,id):
        cls.objects.get(user_id=id)

    @classmethod
    def delete_profile(cls,id):
        cls.objects.filter(id).delete()


    @classmethod
    def search_by_name(cls, searched_name):  
        username = cls.objects.filter(username__icontains=searched_name)
        return username





class Image(models.Model):
    image= models.ImageField(upload_to = 'media/',default="")
    imageName= models.CharField(max_length =60)
    imageCaption= models.TextField()
    profile =models.ForeignKey(Profile,on_delete= models.CASCADE,null = True)
    likes = models.PositiveIntegerField(default = 0)
    follow = models.PositiveIntegerField(default = 0)
    comment = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.imageName

    
    def post(self):
        self.save()

      
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.get(id=id)
        return image
    @classmethod
    def search_post(cls, imageName):
        return cls.objects.filter(img_name__img__name__icontains=imageName)

    @classmethod
    def get_single_photo(cls,id):
        image = cls.objects.get(pk=id)
        return image
        
    @classmethod
    def display_images(cls):
        image = cls.objects.all()
        return image

    @classmethod
    def update_caption(cls,id,new_caption):
        cls.objects.filter(id=id).update(imageCaption=new_caption)  
        

    @classmethod
    def delete_image(cls,id):
        cls.objects.filter(id=id).delete()



class Comments(models.Model):
    comment= models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image=models.ForeignKey(Image, on_delete=models.CASCADE,default='')
    user= models.ForeignKey(Profile, on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.comment
    
    def save_comment(self):
        self.save()
    
        
    @classmethod
    def get_comments(cls,image):
        comments = cls.objects.filter(image__icontains=image)
        return comments
    

    @classmethod
    def delete_comment(cls,id):
        cls.objects.filter(id).delete()

class NewsLetterRecipients(models.Model):
         name = models.CharField(max_length = 30)
         email = models.EmailField()




