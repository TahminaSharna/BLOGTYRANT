from django.urls import path
from App_Blog import views

app_name= 'App_Blog'
urlpatterns = [

path(' ', views.blog_list),
path('edit/<pk>/', views.UpdateBlog.as_view(), name='edit_blog'),
path('details/<slug:slug>', views.blog_details, name='blog_details'),
]
