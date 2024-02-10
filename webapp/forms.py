from django import forms
from webapp.models import Ads


class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ['image', 'description', 'title', 'category', 'price', 'status']
        widgets = {'status': forms.CheckboxSelectMultiple}