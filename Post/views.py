from typing import List
from django.shortcuts import render, redirect
from django.db.models import Q
from Post.forms import FriendRequestForm, FriendRequestResponseForm, PostForm
from User.models import User, Friendship
from .models import Post


def home(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            user = request.user
            username = user.username
            friendships = Friendship.objects.filter(
                Q(user_id=user, status='a') | Q(friend_id=user, status='a')
            )
            friends = []
            for friendship in friendships:
                if friendship.user_id == user:
                    friends.append(friendship.friend_id)
                else:
                    friends.append(friendship.user_id)

            friend_objects = User.objects.filter(id__in=[friend.id for friend in friends])
            friend_objects= list(friend_objects)
            friend_objects.append(user)
            posts = Post.objects.filter(author__in=friend_objects).order_by('-created_at')

            return render(request=request, template_name="post/home.html",
                          context={"username": username, "friends": friend_objects, "posts": posts})
    return redirect("login")


def fiend_friends(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = FriendRequestForm(request.POST)

            if form.is_valid():
                user = request.user
                user_id = form.cleaned_data['user_id']
                friend = User.objects.get(id=user_id)
                friendship = Friendship(user_id=user, friend_id=friend)
                friendship.save()

        user = request.user
        friends_ids = user.friend_request_sent.values_list('friend_id', flat=True)
        users_not_friends = User.objects.exclude(
            Q(id__in=friends_ids) | Q(id=user.id)
        )

        users = User.objects.all()

        return render(request=request, template_name="post/find_friends.html",
                      context={"users": users_not_friends})
    return redirect("login")


def friend_request(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = FriendRequestResponseForm(request.POST)

            if form.is_valid():
                user = request.user
                user_id = form.cleaned_data['user_id']
                status = form.cleaned_data['status']
                friendship = Friendship.objects.get(user_id=user_id, friend_id=user, status='p')
                if status:
                    friendship.status = 'a'
                    friendship.save()
                else:
                    friendship.status = 'r'
                    friendship.save()
        user = request.user
        friend_request_received = Friendship.objects.filter(friend_id=user, status='p')
        friend_request_senders: list[User] = [friendship.user_id for friendship in friend_request_received]
        return render(request=request, template_name="post/friend_request_received.html",
                      context={"users": friend_request_senders})
    return redirect("login")


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            author = request.user
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post_image = form.cleaned_data['post_image']
            post = Post.objects.create(author=author, title=title, content=content, post_image=post_image)
            return redirect("home")

    form = PostForm()

    return render(request=request, template_name="post/create_post.html", context={"form": form})
