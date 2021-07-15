from django.views.generic import CreateView, DetailView
from .forms import SignupForm
from .models import User
from django.urls import reverse
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm


class LoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse('user-detail', args = (self.request.user.pk,))


class UserDetailView(DetailView):
    template_name = 'user-detail.html'
    queryset = User.objects.all()
    context_object_name = 'users'


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignupForm

    def get_success_url(self):
        return reverse('login')