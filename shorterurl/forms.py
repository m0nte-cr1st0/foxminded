from typing import Optional

from django.db.models.query import QuerySet
from django.forms import ModelForm

from .models import ShortUrl


class UrlForm(ModelForm):
    class Meta:
        model = ShortUrl
        fields = ("url",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['url'].widget.attrs.update({
            'autocomplete': 'off',
            'id': "shorten_url",
            'class': "shorten-input",
            'name': "url",
            'value': "",
            'placeholder': "Shorten your link"
        })
        self.fields['url'].widget.input_type = "text"
