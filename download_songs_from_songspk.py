import argparse
import os
import sys
import re
import urllib2
import random
import threading
import time
import logging
import subprocess as sub
from Queue import Queue

from BeautifulSoup import BeautifulSoup as bs


MUSIC_FOLDER = '/data/MEDIA/Music/'
main_thread = threading.currentThread()
main_thread.setName('iTune Downloader')


class DownloadSong(object):

    def __init__(self, args):
        for key, value in args.iteritems():
            setattr(self, key, value)
        logging.basicConfig(
            level=logging.DEBUG if self.debug else logging.INFO,
            format="[%(asctime)s][%(levelname)-6s][%(threadName)-30s] :: %(message)s",
        )
        self.log = logging.getLogger()
        self.log.debug("Parameters set to %s" % (self.__dict__))
        self.command_queue = Queue()
        self.thread = min(5, self.thread)

    def _get_content(self):
        try:
            if self.file:
                response = open(self.file).read()
            else:
                headers = {'User-Agent': 'Mozilla/5.0'}
                req = urllib2.Request(self.url, None, headers)
                response = urllib2.urlopen(req).read()
            return response
        except IOError as e:
            self.log.error("Invalid file/url")
            sys.exit(1)

    def get_song_list(self):
        soup = bs(self._get_content())
        songs = soup.findAll('a', href=re.compile("http(s)?://.*.mp3$"))
        if not songs:
            # TYPE : http://link.songspk.tv/link/song.php?songid=6549
            songs = soup.findAll(
                'a', href=re.compile("http(s)?://.*?songid=.*"))
        return [(y.text.strip(), y.attrMap.get('href')) for y in songs]

    def get_folder_name_from_url(self):
        create_dir_if_not_exists = lambda dir_path: os.makedirs(
            dir_path) if not os.path.isdir(dir_path) else 1
        folder_name = os.path.join(
            self.destination or MUSIC_FOLDER, (self.url or self.file).split('/')[-1].split('.')[0],)
        create_dir_if_not_exists(folder_name)
        return folder_name

    def save_songs_to_disk(self, songs):
        folder = self.get_folder_name_from_url()
        self.log.info(
            "Downloading starts... You can find it here(%s)." %
            (folder))
        for s_name, s_url in songs:
            file_name = "-".join((s_name or s_url.split('/')
                                  [-1]).replace('-', '').split())
            path = os.path.join(folder, file_name +
                                ('.mp3' if not file_name.endswith('.mp3') else ''))
            self.command_queue.put((path, s_url,))

    def downloadEnclosures(self, i):
        """This is the worker thread function.
        It processes items in the queue one after
        another.  These daemon threads go into an
        infinite loop, and only exit when
        the main thread ends.
        """
        while True:
            path, s_url = self.command_queue.get()
            self.processesor(path, s_url)
            time.sleep(1)
            self.command_queue.task_done()
            if self.command_queue.empty():
                self.log.debug('Queue emptied, all done ;)')
                break

    def processesor(self, path, s_url):
        cmd = ["wget", "-c", "'%s'" % (s_url), "-O", "'%s'" % (path)]
        cmd = " ".join(cmd)
        self.log.debug('started downloading : %s' % (cmd))
        if not self.fake:
            p = sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
            output, error = p.communicate()
            if error:
                self.log.error(error)

    def enqueue(self):
        songs = self.get_song_list()
        self.log.info("%d songs found..." % (len(songs)))
        self.save_songs_to_disk(songs)
        # Set up some threads to fetch the enclosures
        for i in range(self.thread):
            worker = threading.Thread(
                target=self.downloadEnclosures, args=(i,))
            worker.setDaemon(True)
            worker.start()
        self.command_queue.join()


def main():
    parser = argparse.ArgumentParser(
        description='Refill your iTune library if you have missed it.')
    group_content = parser.add_mutually_exclusive_group(required=True)
    group_content.add_argument(
        '-f',
        '--file',
        help='If you have direct file of the content html')
    group_content.add_argument(
        '-u', '--url', help='URL of the folder to download')
    parser.add_argument(
        '-t',
        '--thread',
        type=int,
        default=3,
        help='Max length of parallel running thread')
    parser.add_argument(
        '-s',
        '--song-of-the-day',
        help='It will fetch the list of songs from songs-of-the-day category',
        required=False)
    parser.add_argument(
        '-r',
        '--recursive',
        help='If the url/file contains link for another file',
        required=False)
    parser.add_argument(
        '-z',
        '--destination',
        help='Configure the destination of the files',
        required=False)
    parser.add_argument(
        '-d',
        '--debug', action='store_true',
        help='If you want the debug level info',
        required=False)
    parser.add_argument(
        '-x',
        '--fake', default=False,
        help='If you just want to fake the actual download to test the url',
        required=False)
    args = vars(parser.parse_args())
    dl = DownloadSong(args)
    dl.enqueue()

if __name__ == '__main__':
    main()
