from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from appTwo import views
app_name="appTwo"
urlpatterns = [
    
    url(r'^newapp/$',views.task, name="app"),
    url(r'^user/$',views.userinfo, name="userinfo"),
    url(r'^forms/$',views.form_name_view, name="forms"),
    url(r'^signin/$',views.new_user_form,name="signin"),
    url(r'^others/$',views.others,name="others"),
    url(r'^tempFilter/$',views.template_filter,name="tempFilter"),
    url(r'^register/$',views.register,name="register"),
    url(r'^user_login/$',views.user_login,name="user_login"),
    url(r'^user_logout/$',views.user_logout,name="user_logout"),
   

 ]
