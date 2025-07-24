from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main.models import *
from django_ckeditor_5.widgets import CKEditor5Widget

class CustomSignup(UserCreationForm):
    email = forms.EmailField(required= True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class':'form-control'}),
        }

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = [
            'name',
            'poster',
            'DateOfRelease',
            'RottenTomatoes',
            'BoxOfficeCollection',
            'category',
            'actors',
            'rating',
            'director'
        ]

        widgets = {
           'DateOfRelease': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            # 'actors': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }
        def __init__(self, *args, **kwargs):
            super(MovieForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                if not isinstance(self.fields[field].widget, forms.CheckboxSelectMultiple):
                    self.fields[field].widget.attrs.update({'class': 'form-control'})



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
              "text": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
          }
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["content"].required = False