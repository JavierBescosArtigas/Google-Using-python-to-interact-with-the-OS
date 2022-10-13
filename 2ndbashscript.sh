#!/bin/bash

#este script te muestra las 5 lineas del log más repetidas de cada log
for logfile in /var/log/*log; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
