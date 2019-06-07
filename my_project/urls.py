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


import my_flat.views as my_flat_views
import renovation_costs.views as ren_costs_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_site'),
    path('register/', user_views.Register.as_view(), name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login_page.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout_page.html'), name='logout'),
    path('', my_flat_views.MainPage.as_view()),
    path('bud_investment', my_flat_views.DevInvestmentBud.as_view()),
    path('dd_investment', my_flat_views.DevInvestmentDD.as_view()),
    path('victoria_investment', my_flat_views.DevInvestmentVictoria.as_view()),
    path('forum/topic/<int:pk>/', my_flat_views.PostsListView.as_view(), name='forum-topic-posts'),
    path('forum/', my_flat_views.ForumView.as_view(), name='main-forum'),
    path('forum/new_topic/', my_flat_views.CreateNewTopic.as_view(), name='new-topic'),
    path('forum/new_post/<int:pk>', my_flat_views.CreatePostView.as_view(), name='create-post'),
    path('forum/update/<int:pk>', my_flat_views.UpdatePostView.as_view(), name='update-post'),
    path('forum/delete/<int:pk>', my_flat_views.DeletePostView.as_view(), name='delete-post'),
    path('forum/delete_topic/<int:pk>', my_flat_views.DeleteTopicView.as_view(), name='delete-topic'),
    path('renovation_cost', ren_costs_views.RenovationCategoriesView.as_view(), name='renovation-cost'),
    path('renovation_cost/painting', ren_costs_views.PaintingCostView.as_view(), name='painting-cost'),
    path('renovation_cost/paperhanging', ren_costs_views.WallpaperCostView.as_view(), name='wallpaper-cost'),
    path('renovation_cost/ceramic_glaze', ren_costs_views.CeramicGlazeCostView.as_view(), name='ceramicGlaze-cost'),
    path('renovation_cost/plaster', ren_costs_views.PlasterCostView.as_view(), name='plaster-cost'),
    path('renovation_cost/floor_panel', ren_costs_views.FloorPanelCostView.as_view(), name='floor-panel-cost'),





]
