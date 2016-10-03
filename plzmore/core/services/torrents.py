import os
import transmissionrpc

from django.conf import settings


class TorrentService:
    def __init__(self):
        self._tc = transmissionrpc.Client(
            settings.TRANSMISSION_HOST,
            port=settings.TRANSMISSION_PORT
        )

    def add_torrent(self, hash_or_path):
        if os.path.isfile(hash_or_path):
            self.torrent = self.add_torrent_file(hash_or_path)
        else:
            self.torrent = self._tc.get_torrent(hash_or_path)
        return self.torrent

    def add_torrent_file(self, torrent_path, autostart=False):
        self.torrent = self._tc.add_torrent(
            torrent_path,
            paused=not autostart
        )
        return self.torrent

    def get_files(self):
        self.files_dict = {}
        for file_dict in self._tc.get_files(self.torrent.hashString).values():
            self.files_dict.update(file_dict)
        return self.files_dict

    def get_files_unwanted(self):
        if not hasattr(self, 'files_dict'):
            self.get_files()
        files_unwanted = []
        for file_id, file_info in self.files_dict.items():
            should_download = (
                file_info.get('name').endswith('.mkv') and
                'sample' not in file_info.get('name').lower()
            )
            if not should_download:
                files_unwanted.append(file_id)
        return files_unwanted

    def _download(self):
        files_unwanted = self.get_files_unwanted()
        print(files_unwanted)
        if files_unwanted:
            self._tc.change_torrent(
                self.torrent.hashString,
                files_unwanted=files_unwanted
            )
        self.torrent.start()

    def download_torrent(self, path):
        self.add_torrent_file(path)
        self._download()
