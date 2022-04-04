from unicodedata import name
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
# from django.conf import settings


urlpatterns = [

path('',views.landingpage,name='landing_page'),
path('signup',views.signUp,name='signup'),
# path('login',views.sighnUp,name='signup'),
path('landing/post',views.new_post,name='new_post'),
path('moreonpic/<int:id>',views.more,name='morepic'),
path('showComments/<imageName>',views.comments,name='showComments'),
path('showProfile',views.profile,name='showProfile'),
path('showProfile/update/<int:id>',views.uprofile,name='uprofile'),
path('searched',views.searchprofile,name='searched'),
path('landing/new_comment/<int:id>',views.new_comment,name='new_comment'),
path('delete/<int:id>',views.delete_ipost,name='delete'),
path('update_caption/<int:id>',views.update_caption,name='updateCaption')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)