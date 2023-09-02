from django.urls import path

from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("find_friends", views.fiend_friends, name="find_friends"),
    path("friend_request", views.friend_request, name="friend_request"),
    path("create_post", views.create_post, name="create_post")
]
