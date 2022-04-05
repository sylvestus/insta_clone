from django.test import TestCase
from .models import Profile, Image, User, Comments

# Create your tests here.

class CommentsTest(TestCase):

    def setUp(self):
        self.new_user =  User(username='silvano36', email='silvanussigei19960@gmail.com', password='123456')
        self.new_user.save()
        self.new_image = Image(image_name='cite', image='cite.pngg', image_caption='great work guys', profile=self.new_user)
        self.new_image.save()
        self.new_comment = Comments(comment='cant say enough thank you people',image=self.new_image,user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comments))

    def test_save_comment(self):
        self.new_comment.save_comment()
        comment = Comments.objects.all()
        self.assertTrue(len(comment)>0)

class ProfileTest(TestCase):

    def setUp(self):
        self.new_user = User(username='silvano36', email='silvanussigei19960@gmail.com', password='123456')
        self.new_user.save()
        self.new_profile = Profile(profile_image='cite.png', bio='the best man in planet earth', user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
    
   # Create your tests here.
class ImageTest(TestCase):

    def setUp(self):
        self.new_user =  User(username='silvano36', email='silvanussigei19960@gmail.com', password='123456')
        self.new_user.save()
        self.new_profile = Profile(profile_image='cite.png', bio='you know who it is', user=self.new_user)
        self.new_profile.save()
        self.new_image = Image(image_name='cite', image='cite.pngg', image_caption='i love my work', profile=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_image(self):
        self.new_image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image)>0)

    

