from django import forms


class UploadTorrentForm(forms.Form):
    torrent = forms.FileField(
        label='Select a torrent',
        help_text='Select a torrent to upload.'
    )
