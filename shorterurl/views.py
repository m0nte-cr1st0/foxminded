from typing import Optional

from django.conf import settings
from django.db.models import F, QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, RedirectView

from .forms import UrlForm
from .models import ShortUrl


class ShortUrlCreateView(CreateView):
    form_class = UrlForm
    template_name = "shorterurl/create.html"

    def form_invalid(self, form):
        url: Optional[QuerySet[ShortUrl]] = ShortUrl.objects.filter(url=form.data["url"])
        if url.exists():
            return HttpResponseRedirect(reverse("url-detail", args=(url.first().pk,)))


class ShortUrlDetailView(DetailView):
    model = ShortUrl


class ShortUrlRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        short_url = settings.SITE_URL + kwargs['short_url']
        url = get_object_or_404(ShortUrl, short_url=short_url)
        url.update_counter()
        return url.url
