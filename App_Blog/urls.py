from django.urls import path
from App_Blog import views

app_name= 'App_Blog'
urlpatterns = [

path(' ', views.blog_list),
path('edit/<pk>/', views.UpdateBlog.as_view(), name='edit_blog'),
path('liked/<pk>/', views.liked, name='liked_post'),
path('unliked/<pk>/', views.unliked, name='unliked_post'),
path('details/<slug:slug>', views.blog_details, name='blog_details'),
]
