import os

from django.conf import settings
from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--hash', nargs=1, type=str,
                            help="The torrent's hash.",
                            default=None)
        parser.add_argument('--location', nargs=1, type=str,
                            help="Path to the download location.",
                            default=None)
        parser.add_argument('--name', nargs=1, type=str,
                            help="The name of the torrent.",
                            default=None)

    def handle(self, *args, **options):
        print(options['hash'])
        print(options['location'])
        print(options['name'])
        path_to_write = os.path.join(
            settings.MEDIA_ROOT, 'test.txt'
        )
        with open(path_to_write, 'w+') as f:
            f.write(options['hash'][0])
            f.write("\n")
            f.write(options['location'][0])
            f.write("\n")
            f.write(options['name'][0])
        # conf_files_path = os.path.join(
        #     os.path.dirname(__file__),
        #     '*.mkv'
        # )
        # conffiles = glob.glob(conf_files_path)
        # conffiles.sort()
