source /Users/ollandos/small-site/plzmore-env/bin/activate & wait
/Users/ollandos/small-site/plzmore/manage.py prepare_video \
--hash $TR_TORRENT_HASH \
--location $TR_TORRENT_DIR \
--name $TR_TORRENT_NAME
