from django.conf import settings
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  'bio',
                  'location',
                  'birth_date',
                  'picture',
                  'job_title',
                  'personal_url',
                  'facebook_account',
                  'twitter_account',
                  'github_account',
                  'linkedin_account'
                  )


class UserUpdateForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'required': True}),
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'picture', 'job_title', 'location', 'personal_url',
                  'facebook_account', 'twitter_account', 'github_account',
                  'linkedin_account', 'bio', ]
