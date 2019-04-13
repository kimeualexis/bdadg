from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='users-index'),
    path('add-profile', views.ProfileCreateView.as_view(), name='add-profile'),
    path('<int:pk>/update-profile', views.ProfileUpdateView.as_view(), name='update-profile'),
    path('<int:pk>/delete-profile', views.ProfileDeleteView.as_view(), name='delete-profile'),
]