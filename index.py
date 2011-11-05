# module to help import and track videos

import sqlite3
import os
import os.path
import re
import sys

good_extensions = ['avi','mp4','mkv', 'm4v']

regex = ('(?P<nm>.*)'+ # get name
    '\\.'+ # dividing .
    '[sS]?(?P<sn>\d{1,2})[eEx](?P<ep>\d{1,2})') # S01E01 format

db = sqlite3.connect("videos.db")
c = db.cursor()

def index(directory):
    files = os.listdir(directory)
    for fname in files:
        name, ext = os.path.splitext(fname)
        if ext[1:] not in good_extensions:
            continue
        matches = re.match(regex, name)
        c.execute('insert into videos(show, path, type, season, episode) values(?,?,?,?,?)', (matches.group(1), os.path.join(directory,fname), 'show', matches.group('sn'), matches.group('ep')))
    db.commit()
    c.close()

index(sys.argv[1])
