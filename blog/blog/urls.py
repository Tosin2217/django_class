"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
# from daily_news.views import Hello
from daily_news.views import (
    Dashboard,blog_post,homepage,
    article,not_found,edit_blog,
    register, delete_blog, profile)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Dashboard/',Dashboard),
    path("blog/", blog_post, name="create-blog"),
    path("article/<int:pk>/", article, name="read-blog"), 
    path("article/<int:pk>/edit/", edit_blog, name="edit-blog"),
    path("accounts/register", register, name="register"),
    path("accounts/profile", profile, name='profile'),
    path("article/<int:pk>/delete/", delete_blog, name="delete-blog"),
    path("", homepage, name='home'),
    path("not_found/", not_found),
    path("accounts/", include('django.contrib.auth.urls'))
]
