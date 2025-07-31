from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_main, name="blog_index"),
    path("post/<id>", views.post, name="post"),
    path("image/<id>", views.image, name="image"),
]
