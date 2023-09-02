from django import forms
from .models import Post


class FriendRequestForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.HiddenInput())


class FriendRequestResponseForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.HiddenInput())
    status = forms.BooleanField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'post_image']


