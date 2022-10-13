#!/usr/bin/env python3
import os
dir = os.getcwd()
for name in os.listdir(dir):
    fullname = os.path.join(dir,name)
    if os.path.isdir(fullname):
        print("{} es un directorio" .format(fullname))
    else:
        print("{} es un archivo" .format(fullname))
