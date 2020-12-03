import tarfile
from os import path
from glob import glob

homedir = path.dirname(path.dirname(path.realpath(__file__)))
imagedir = path.join(homedir, 'media', 'images')

distname = 'datasets+img'
distfile = path.join(homedir, distname + '.tar.gz')

tar = tarfile.open(distfile, "w:gz")

readmefile = path.join(homedir, 'README.md')
tar.add(readmefile, arcname=path.join(distname, path.split(readmefile)[1]))
    
jsonfiles = glob(path.join(homedir, '*.json'))
csvfiles = glob(path.join(homedir, '*.csv'))
for file in csvfiles + jsonfiles:
    tar.add(file, arcname=path.join(distname, path.split(file)[1]))

jpgfiles = glob(path.join(imagedir, '*.jpg'))
for file in jpgfiles:
    tar.add(file, arcname=path.join(distname, 'media/images',
                                    path.split(file)[1]))

tar.close()

print('Dist file saved in', distfile)
