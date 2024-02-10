from django import forms
from webapp.models import Ads, Comment


class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ['image', 'description', 'title', 'category', 'price', 'status']
        widgets = {'status': forms.RadioSelect}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )