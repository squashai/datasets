from os import path
from glob import glob
from math import floor, log10
import json
import csv

homedir = path.dirname(path.dirname(path.realpath(__file__)))

datasets = glob(path.join(homedir, '*.json'))

with open(path.join(homedir, 'positions.csv'), 'w') as playerscsv, \
     open(path.join(homedir, 'attributes.csv'), 'w') as infocsv:

    playerswriter = csv.writer(playerscsv, delimiter=';')
    playerswriter.writerow([
        'filename', 'p1.x', 'p1.y', 'p2.x', 'p2.y'
    ])
    infowriter = csv.writer(infocsv, delimiter=';')
    infowriter.writerow([
        'filename', 'action', 'replay',
        'p1.name', 'p1.color', 'p2.name', 'p2.color'
    ])
    
    for datafile in datasets:
        with open(datafile) as fd:
            data = json.load(fd)

            id = path.split(datafile)[1][:-5]

            tlen = 1
            for label in data['labels']:
                if label['time'] > 0:
                    tlen = max(tlen, floor(log10(label['time'] * 1000)) + 1)

            for label in data['labels']:
                time = label['time'] * 1000
                imagefile = path.join('media/images',
                                      '%s-%0*d.jpg' % (id, tlen, time))
                p1 = label['players']['1']
                p2 = label['players']['2']
                playerswriter.writerow([
                    imagefile,
                    p1['x'] if p1['visible'] else None,
                    p1['y'] if p1['visible'] else None,
                    p2['x'] if p2['visible'] else None,
                    p2['y'] if p2['visible'] else None
                ])
                        
                infowriter.writerow([
                    imagefile, label['action'], label['replay'],
                    p1['name'] if p1['visible'] else None,
                    p1['color'] if p1['visible'] else None,
                    p2['name'] if p2['visible'] else None,
                    p2['color'] if p2['visible'] else None
                ])
    
