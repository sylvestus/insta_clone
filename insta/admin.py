
from django.contrib import admin

from insta.models import Comments, Profile,Image

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comments)