# flake8: noqa

ENCODING_CMDS = {
    'mkv_mp4': {
        'enc_sound': 'ffmpeg -i {input}.mkv -c:v copy -c:a libfaac {output}.mp4',
        'cp_sound': ''
    }
}

DOWNLOAD_ROOT = os.path.join(BASE_DIR, 'downloads/')
