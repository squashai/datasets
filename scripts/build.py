from os import path, makedirs, listdir
from glob import glob
from urllib import request
from urllib.request import urlretrieve
from math import floor, log10
import json
import ssl
import cv2
import re

ssl._create_default_https_context = ssl._create_unverified_context

opener = request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
request.install_opener(opener)

homedir = path.dirname(path.dirname(path.realpath(__file__)))
videodir = path.join(homedir, 'media', 'videos')
imagedir = path.join(homedir, 'media', 'images')

makedirs(videodir, exist_ok=True)
makedirs(imagedir, exist_ok=True)

def download(url, filename):
    if not path.exists(filename):
        print('saving %s into %s' % (url, filename))
        urlretrieve(url, filename)
        print('saved')

datasets = glob(path.join(homedir, '*.json'))

for s in datasets:
    with open(s) as f:
        data = json.load(f)
        filename=path.join(videodir, data['source']['name'])
        download(url=data['source']['url'], filename=filename)
        vidcap = cv2.VideoCapture(filename=filename)
        id = re.match('[^.]*', data['source']['name']).group()
        tlen = 1
        for l in data['labels']:
            if l['time'] > 0:
                tlen = max(tlen, floor(log10(l['time'] * 1000)) + 1)

        print('Len for %s: %d' % (id, tlen))
                
        for l in data['labels']:
            ts = l['time'] * 1000
            vidcap.set(cv2.CAP_PROP_POS_MSEC, ts)
            success, image = vidcap.read()
            if success:
                cv2.imwrite(path.join(imagedir, '%s-%0*d.jpg' % (id, tlen, ts)),
                            image)

