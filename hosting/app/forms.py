# from django import forms
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# # from .models import DbmsProjectData

# from django.db import models
# from django.db.models import Model

from app.models import Books,author

from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms.widgets import TextInput

User = get_user_model()


class RegisterForm(forms.ModelForm):
    """
    The default 

    """    
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['email', 'branch', 'year', 'username']

    def clean_email(self):
        '''
        Verify email is available.
        '''
        # print('aryan')
        email = self.cleaned_data.get('email')
        qs = User.user_obj.filter(email=email)
        if qs.exists():
            # print("chicken")
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        '''
        Verify both passwords match.
         '''        
        data = self.cleaned_data
        password = str(self.cleaned_data.get("password"))
        password_2 = str(self.cleaned_data.get("password_2"))

        if password != password_2:
            raise forms.ValidationError("Passwords don't match")
        return data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        # fields = ['email', 'password', 'is_active', 'is_admin']
        exclude = ['is_active']


    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
    
class GetAuthor(forms.ModelForm):
    class Meta:
        model=author
        fields=['aname']




        # widgets={
        #     'aname':forms.TextInput(attrs={'class':'form-control'}),
        # }


class BookForm(forms.ModelForm):
    class Meta:
        model= Books
        fields=['name','genre','img']
    widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        
        'genre':forms.Select(attrs={'class':'form-select'}),
        'img':forms.FileInput(attrs={'class':'form-control'}),
    }
    
