from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('message', 'author',)
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Your name'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter your comment here'}),
        }








