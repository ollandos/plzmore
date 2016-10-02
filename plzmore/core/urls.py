from django.conf import urls

from plzmore.core import views

urlpatterns = [
    urls.url(
        r'^video/(?P<plzid>[A-Za-z0-9\-\_]{11})/$',
        views.StreamView.as_view()
    ),
    urls.url(
        r'^torrent/upload/$',
        views.UploadTorrentView.as_view()
    ),
]
