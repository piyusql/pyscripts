import os
import sys
import re
import urllib
import random
import threading
import time
import logging
import subprocess as sub

from BeautifulSoup import BeautifulSoup as bs

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s][%(levelname)-6s][%(threadName)-30s] :: %(message)s",)
MUSIC_FOLDER = '/data/MEDIA/Music/'


class DownloadSong(object):

    def __init__(self, url):
        self.url = url

    def get_song_list(self):
        response = urllib.urlopen(self.url).read()
        soup = bs(response)
        songs = soup.findAll('a', href=re.compile(r'http://.*\?songid.*'))
        return [(y.text.strip(), y.attrMap.get('href')) for y in songs]

    def get_folder_name_from_url(self):
        create_dir_if_not_exists = lambda dir_path: os.makedirs(dir_path) if not os.path.isdir(dir_path) else 1
        folder_name = os.path.join(MUSIC_FOLDER, self.url.split('/')[-1].split('.')[0],)
        create_dir_if_not_exists(folder_name)
        return folder_name

    def save_songs_to_disk(self, songs):
        folder = self.get_folder_name_from_url()
        print "\nIt will download %d songs, you can find it here(%s).\n" %(len(songs), folder)
        for s_name, s_url in songs:
            path = os.path.join(folder, "-".join(s_name.split()) + '.mp3')
            self.download_song(path, s_url)

    def download_song(self, path, s_url):
        cmd = "wget %s -O %s" % (s_url, path)
        t = threading.Thread(name=os.path.basename(path), target=self.downloader, args=(cmd,))
        t.setDaemon(True)
        t.start()

    def downloader(self, cmd):
        """thread worker function"""
        t = threading.currentThread()
        logging.debug('started downloading')
        p = sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
        output, error = p.communicate()
        logging.debug('finished downloading')


if __name__ == '__main__':
    url = sys.argv[1]
    dl = DownloadSong(url)
    songs = dl.get_song_list()
    dl.save_songs_to_disk(songs)
    # wait for all thread to complete work
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        logging.debug('waiting to complete... %s', t.getName())
        t.join()
