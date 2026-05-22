from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name="home"),
    path("posts/", views.posts, name="posts"),
    path("post/add/", views.post_new, name="add_post"),
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
    path("posts/<int:pk>/delete/", views.post_delete, name="post_delete")
]
