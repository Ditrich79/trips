from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', BlogHome.as_view(), name='index'),
    path('article/<slug:article_slug>/', ShowArticle.as_view(), name='article'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
    path('addarticle/', AddArticle.as_view(), name='add_article'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]
