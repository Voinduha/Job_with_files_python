import os
import zipfile

zip_ = zipfile.ZipFile("myzipfile.zip", "w")
for dirname, subdirs, files in os.walk('resources'):
    zip_.write(dirname)
    for filename in files:
        zip_.write(os.path.join(dirname, filename))
zip_.close()