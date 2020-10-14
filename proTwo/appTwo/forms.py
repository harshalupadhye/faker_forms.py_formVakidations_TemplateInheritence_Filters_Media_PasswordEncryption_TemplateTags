from django import forms
from django.core import validators
from appTwo.models import Users,UserProfileInfo     #this is model that has to be converted to form 
from django.contrib.auth.models import User
"""
this is custom validation without database connected 
"""
def check_for_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError("please start the name with z")



    
class FormName(forms.Form):
    name=forms.CharField(validators=[check_for_z])
    email=forms.EmailField(required=True)
    verify_email=forms.EmailField(label="Enter the email again")
    text=forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("gotcha MF")
    #     return botcatcher
    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        verify_email=all_clean_data['verify_email']
        # name=all_clean_data['name']
        if email !=verify_email:
            raise forms.ValidationError("Email is not matching")
        # if name[0].lower()!='z':
        #     raise forms.ValidationError("name should start with z")
"""
this code is now for the model to connect with the database 
"""
class NewUserForm(forms.ModelForm):
    verify_email=forms.EmailField()
    class Meta():
        model=Users
        fields='__all__'
    def clean_verify_email(self):
            verify_email=self.cleaned_data['verify_email']
            all_clean_data=super().clean()
            email=all_clean_data['email']
            if verify_email!=email:
                raise forms.ValidationError("email not matching")
       
            
        
   
        
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User  
        fields=('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')
   
   
        


    