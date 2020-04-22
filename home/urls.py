
from django.urls import re_path
from .views import HomePageView
from django.contrib.auth import views as auth_views
urlpatterns = [
    re_path(r'^$', HomePageView.as_view(), name='homepage'),
    re_path(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
