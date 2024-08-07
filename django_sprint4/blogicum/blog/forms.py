from django import forms
from django.contrib.auth import get_user_model

from .models import Category, Comment, Location, Post


User = get_user_model()


class PostForm(forms.ModelForm):
    location = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        widget=forms.RadioSelect,
        label='Местоположение'
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.RadioSelect,
        label='Категория'
    )

    pub_date = forms.DateTimeField(
        input_formats=['%m-%-%Y %H-%M'],
        widget=forms.DateInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'}
        ),
        label='Дата и время публикации'
    )

    class Meta:
        model = Post
        exclude = ('author',)


class UserEditForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
            'text': forms.Textarea(
                {'cols': '22', 'rows': '5'}
            )
        }
