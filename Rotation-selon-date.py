#!/usr/bin/python3

#ROTATION DES FICHIER 
import os, time

path = r"chemin de votre répertoire qui contient vos documents"
now = time.time()

for filename in os.listdir(path):
    # if os.stat(os.path.join(path, filename)).st_mtime < now - 1 * 86400:
    if os.path.getmtime(os.path.join(path, filename)) < now - 1 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            print(filename)
            os.remove(os.path.join(path, filename))