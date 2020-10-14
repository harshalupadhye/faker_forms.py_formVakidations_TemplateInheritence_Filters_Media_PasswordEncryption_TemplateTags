from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from appTwo.models import Topic,Webpage,AccessRecord,Users,UserProfileInfo
from appTwo import forms
from appTwo.forms import NewUserForm,UserForm,UserProfileInfoForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import requests



# Create your views here.
def index(request):
    return render(request,"appTwo/main.html")
   
def task(request):
    webpgs=AccessRecord.objects.order_by('date')
    access={'access_record':webpgs}
    
    return render (request,'appTwo/index.html', context=access)
def userinfo(request):
    usersin=Users.objects.order_by('fname')
    # user_dict={'user_records':usersin}
    webpgs=AccessRecord.objects.order_by('date')
    # access={'access_record':webpgs}
    
    
    return render(request,'appTwo/userinfo.html',{'user_records':usersin,'access_record':webpgs})

def form_name_view(request):
    form=forms.FormName()
    if request.method == 'POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])
    return render(request,"appTwo/form_page.html",{'form':form})
def new_user_form(request):
    form=NewUserForm()
    if request.method == 'POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("form is invalid")
    return render(request,'appTwo/signin.html',{'form':form})
def others(request):
    form=NewUserForm()
    if request.method == 'POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("form is invalid")

    
    return render (request,'appTwo/other.html',{'form':form})

def template_filter(request):
    context_dict={'text':'hello world','number':100}
    return render(request,'appTwo/other.html',context=context_dict)
def register(request):
    registered=False
    
    if request.method == 'POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user #model.py madhe feild ahe one to one 
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'appTwo/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username',False)
        password=request.POST.get('password',False)

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("User not active")
        else:
            print("username: {} and password: {}".format(username,password))
            return HttpResponse("invalid details")
    else:
        return render(request,"appTwo/user_login.html",{})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


