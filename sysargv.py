#!/usr/bin/env python3

import sys
if len(sys.argv) == 1 :
    print('no argumentos enviados')
else:
    print(sys.argv[1:])

for linea in sys.stdin:
    print(linea.strip().capitalize())
#ejecuta echo 'hola mundo' | ./sysargv.py que pasa aquiii
