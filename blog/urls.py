from django.urls import path
from . import views

app_name="blog"
urlpatterns = [
    path('blog/', views.blog,name="article-blog"),
    path('blog/<int:pk>/', views.blog_detail),
    path('example/', views.example),
]