from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': ' ',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': ' ',
                'style': 'height: 180px;'
            }),
        }

        labels = {
            'title': 'Post Title',
            'text': 'Write your content',
        }
