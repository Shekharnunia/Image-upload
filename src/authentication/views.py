from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import UpdateView
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdateForm
from django.urls import reverse
from .models import User


def home(request):
    return render(request, 'home.html', {})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class UserUpdateView(UpdateView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    form_class = UserUpdateForm
    template_name = 'registration/user_form.html'
    # send the user back to their own page after a successful update

    def get_success_url(self):
        return reverse('home',
                       )

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)
