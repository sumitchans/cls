from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^register/$', UserRegisterView.as_view(), name='user-register'),
    url(r'^login/$', UserLoginView.as_view(), name='user-login'),
    url(r'^logout/$', UserLogoutView.as_view(), name='user-logout'),
    url(r'user-class/$', UserClassView.as_view(), name='user-class'),
]