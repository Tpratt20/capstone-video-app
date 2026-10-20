from django import forms
from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'url', 'notes']

#simple form that stores the user's search term
class SearchForm(forms.Form):
    search_term = forms.CharField()