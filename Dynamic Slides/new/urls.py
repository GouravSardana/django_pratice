"""new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from poll.views import AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AboutView.as_view(), name='about'),
    url(r'^login/',include('django.contrib.auth.urls')),
    url(r'^logout/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    # path('publishers/', Publisher.as_view()),
    # path('create/', Author.as_view(), name='view'),
    # path('update/<int:pk>', Author2.as_view(), name='update'),
    # path('delete/<int:pk>', Author3.as_view(), name='delete'),

]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'