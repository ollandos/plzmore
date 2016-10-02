import os
import random
import string

from django.conf import settings


def get_random_plzid(size=11):
    cases = string.ascii_letters + string.digits + '-' + '_'
    return ''.join([random.choice(cases) for _ in range(size)])


def write_uploaded_file(f, plzid, extension=None):
    extension = extension if extension is not None else ''
    final_path = ''.join([
        settings.TORRENT_ROOT,
        plzid,
        extension
    ])
    with open(final_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def download_torrent(plzid):
    torrent_path = ''.join([
        settings.TORRENT_ROOT,
        plzid,
        '.torrent'
    ])
    os.system('bash ~/transmission/scripts/download_torrent.sh {}'.format(
        torrent_path
    ))
