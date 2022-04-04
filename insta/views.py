from email import message
from email.mime import image
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from insta.models import Image, Profile, Comments,NewsLetterRecipients
from .forms import commentForm, newImage, signUp, UprofileForm, UuserForm,NewsletterForms,captionForm
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from django.http import HttpResponse,Http404,HttpResponseRedirect



# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('landing_page')
    else:
        if request.method == 'POST':
            form = signUp(request.POST)
            if form.is_valid():
                form.save()
                
                username = request.get['username']
                first_name = request.get['first_name']
                last_name = request.get['last_name']
                password = request.get['password']
                email = request.get['email']
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name, email=email,password=password)
                user.save()
                return redirect('landing_page')

        else:
            form = signUp()
    return render(request, 'django_registration/registration_form.html', {'form': form})



@login_required(login_url='/accounts/login/')
def landingpage(request):
    images = Image.display_images()
    profile = Profile.objects.all()
    comment = Comments.objects.all()
    current_user = request.user
    if request.method=='POST':
        form=NewsletterForms(request.POST)
        if form.is_valid():
            name=form.cleaned_data['your_name']
            email=form.cleaned_data['email']
            recipient= NewsLetterRecipients(name=name,email=email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('news_today')
    else:
            form=NewsletterForms()
    return render(request,"landingpage.html",{"images": images, "profiles": profile, "comments": comment,'current_user':current_user,"letterForm":form })


def more(request, id):
    message = "more about the pic"
    more_on_image = Image.get_single_photo(id=id)
    comment = Comments.objects.all
    return render(request, "morepic.html", {"message": message,'image':more_on_image,'comments':comment})


def searchprofile(request):
    if "instahandle" in request.GET and request.GET["instahandle"]:
        search_term = request.GET.get("instahandle")
        users = Profile.objects.filter(user__username__icontains = search_term).all()
        posts = Image.objects.filter(imageName__icontains = search_term).all()
        # search_results = User.objects.filter(username__icontains=search_term)
        message = f"{search_term}"
        return render(request,"search.html",{"message": message, "users":users,"posts":posts})

    else:
        message = "You haven't searched for any term"
        return render(request, "searched.html", {"message": message})




@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user

    if request.method == "POST":
        form = newImage(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            imageName = form.cleaned_data["imageName"]
            imageCaption = form.cleaned_data["imageCaption"]
            comment = form.cleaned_data["comment"]
            post = Image(
                image=image,
                imageName=imageName,
                imageCaption=imageCaption,
                comment=comment,
            )
            post.save()
        return redirect("landing_page")

    else:
        form = newImage()
    return render(request, "new_post.html", {"postForm": form})


def delete_ipost(request,id):
    post_delete=Image.objects.get(id=id)
    post_delete.delete()
    return redirect('landing_page')

def update_caption(request,id):
    form = captionForm()
    if request.method == "POST":
        
        if form.is_valid():
            new_caption = form.cleaned_data["new_caption"]
            update_caption(id=id,newcaption=new_caption)
            return redirect('landing_page')
    return render(request,'updateCaption.html',{'captionForm':form})

def new_comment(request, id):
    image= Image.get_image_by_id(id=id)
    current_user = request.user

    form = commentForm()
    if request.method == "POST":
        
        if form.is_valid():
            comment = form.cleaned_data["comment"]
            new_comment = Comments(comment=comment)
            new_comment.save()
        return redirect("landing_page")
    else:
        form = commentForm()
    return render(request, "new_comment.html", {"commentForm": form,"image":image,'current_user':current_user})

# @login_required
# def new_comment(request,id):
#   comment_form = commentForm()
#   post = Image.objects.filter(pk = id).first()
#   if request.method == 'POST':
#     comment_form = commentForm(request.POST)
#     if comment_form.is_valid():
#       comment = comment_form.save(commit = False)
#       comment.user = request.user
#       comment.post = post
#       comment.save()
#   return redirect('landing_page')


def profile(request):
    current_user = request.user
    images = Image.objects.filter(profile=current_user.id).all

    return render(request, "profile.html", {"images": images})

def comments(request,imageName):
    current_user = request.user
    comments = comments.get_comments(imageName =Image.imageName)

    return render(request, "comments.html", {"comments": comments})

@login_required(login_url='/accounts/login/')
def uprofile(request, id):

    user_object = get_object_or_404(User, id=id)
    profile_object = get_object_or_404(Profile, user_id=id)
    profile_update = UprofileForm(request.POST or None, instance=profile_object)
    user_update = UuserForm(request.POST or None, instance=user_object)
    if profile_update.is_valid() and user_update.is_valid():
        user_update.save()
        profile_update.save()
        return redirect("showProfile")

    return render(
        request, "uprofile.html",{"profile_update": profile_update, "user_update": user_update})
