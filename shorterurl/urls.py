from django.urls import path

from shorterurl.views import ShortUrlCreateView, ShortUrlDetailView, ShortUrlRedirectView

urlpatterns = [
    path("", ShortUrlCreateView.as_view(), name="url-create"),
    path("<int:pk>", ShortUrlDetailView.as_view(), name="url-detail"),
    path("<str:short_url>", ShortUrlRedirectView.as_view(url='http://google.com'), name="url-redirect"),
]
