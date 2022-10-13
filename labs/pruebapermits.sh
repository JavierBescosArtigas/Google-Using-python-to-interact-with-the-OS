#!/usr/bin/bash

echo 'introduzca el archivo al que adjudicarle el permiso -rw0 000 000, pero ahora voy a cambiar el permiso al que pases por comando'
read var1
chmod 600 $1
exit 0
