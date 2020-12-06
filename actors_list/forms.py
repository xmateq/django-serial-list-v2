from django import forms
from .models import Serial, Comment


class SerialForm(forms.ModelForm):
    class Meta:
        model = Serial
        fields = ['title', 'release_date']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('com', 'rate')