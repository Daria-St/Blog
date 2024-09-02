from django import forms
from .models import PostCategory

class PostAddForm(forms.Form):
    title = forms.CharField(max_length=500)
    text = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=PostCategory.objects.all())

