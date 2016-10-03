from django import views
from django import shortcuts
from django.http import HttpResponse

# Imaginary function to handle an uploaded file.
from plzmore.core.forms import fileforms
from plzmore.core.services import torrents
from plzmore.core import utils


class UploadTorrentView(views.View):
    def dispatch(self, request, *args, **kwargs):
        return super(UploadTorrentView, self).dispatch(
            request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = fileforms.UploadTorrentForm()
        return shortcuts.render(
            request, 'upload_torrent_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = fileforms.UploadTorrentForm(request.POST, request.FILES)
        if form.is_valid():
            location = utils.write_uploaded_file(
                request.FILES['torrent'],
                utils.get_random_plzid(),
                extension='.torrent')
            ts = torrents.TorrentService()
            ts.download_torrent(location)
            return HttpResponse()
        else:
            return self.get()


class StreamView(views.View):
    def dispatch(self, request, plzid, *args, **kwargs):
        # self.video = shortcuts.get_object_or_404(Video, plzid=plzid)
        return super(StreamView, self).dispatch(
            request, plzid, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return shortcuts.render(request, "player.html", {})
