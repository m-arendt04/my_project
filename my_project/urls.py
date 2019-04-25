"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views

from my_flat.views import MainPage, DevInvestmentBud, DevInvestmentDD, DevInvestmentVictoria, ForumView, PostsListView, \
    CreatePostView, UpdatePostView, DeletePostView, CreateNewTopic, DeleteTopicView
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.Register.as_view(), name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login_page.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout_page.html'), name='logout'),
    path('', MainPage.as_view()),
    path('bud_investment', DevInvestmentBud.as_view()),
    path('dd_investment', DevInvestmentDD.as_view()),
    path('victoria_investment', DevInvestmentVictoria.as_view()),
    path('forum/topic/<int:pk>', PostsListView.as_view(), name='forumTopicPosts'),
    path('forum/', ForumView.as_view(), name='main_forum'),
    path('forum/new_topic', CreateNewTopic.as_view(), name='new_topic'),
    path('forum/new_post/<int:pk>', CreatePostView.as_view(), name='create_post'),
    path('forum/update/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('forum/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('forum/delete_topic/<int:pk>', DeleteTopicView.as_view(), name='delete_topic'),


]
