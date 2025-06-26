from django.urls import path

from . import views

urlpatterns = [
    path("", views.blog_main, name="index"),
    path("blog/post/<id>", views.post, name="post"),
    path("privacy-policy", views.privacy_policy, name="privacy-policy"),
]
