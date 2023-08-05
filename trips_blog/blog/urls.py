from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogHome.as_view(), name='index'),
    path('article/<slug:article_slug>/', ShowArticle.as_view(), name='article'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
    path('addarticle/', AddArticle.as_view(), name='add_article'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
]
