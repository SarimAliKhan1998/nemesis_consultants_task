"""nemesis_consultants_task URL Configuration"""

from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import LoginView, UserDetailView, SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name = 'login'),
    path('users/<int:pk>/', UserDetailView.as_view(), name = "user-detail"),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('signup/', SignupView.as_view(), name = 'signup')
]
