#!/usr/bin/env python3

import sys, os

def find(word, path):
    for files in os.listdir(path):
        if word in files :
            print(path + "/" + files)

        try:
            new_path = os.path.join(path, files)
            find(word, new_path)
        except (FileNotFoundError, NotADirectoryError):
            # print("not a direcotry")
            continue;

# for sys.sys.argv[1] in os.listdir(sys.argv[2]):
#     # if fnmach.fnmatch(file, sys.argv[1]):
#     print (os.path.realpath(file))

find(sys.argv[1], sys.argv[2])
