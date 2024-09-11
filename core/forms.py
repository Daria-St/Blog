from django import forms
from .models import PostCategory, Post
from django.core.exceptions import ValidationError

class PostAddForm(forms.Form):
    title = forms.CharField(max_length=500)
    text = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=PostCategory.objects.all())

class PostAddModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category']

    def __init__(self, *args, **kwargs):
        super(PostAddModelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        category = cleaned_data.get('category')

        if Post.objects.filter(title=title, category=category):
            raise ValidationError('Такой заголовок уже есть  в этой категории!')
        return cleaned_data


class CommentAddForm(forms.Form):
    text = forms.CharField(max_length=1000, label='Текст')

class FeedbackAddForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(FeedbackAddForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    name = forms.CharField()
    text = forms.CharField(max_length=1000, widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data['name'].split()
        if len(name) != 2:
            raise ValidationError('Некорректный ввод имени')
        return name