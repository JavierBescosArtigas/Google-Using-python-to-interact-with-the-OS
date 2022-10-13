#!/bin/bash

#this simple scripts creates the 2 html reports directly, all 3 .py as well as .log files have to be in this Cworking directory
echo 'let\'s read logfile & obtain csvs from it'

python3 tickycheck.py

echo  '2 .csv files should appear in current folder'

mkdir httpfiles
python3 csv_to_html.py usersTohtml.csv ./httpfiles/users.html
python3 csv_to_html.py errorsTohtml.csv ./httpfiles/errors.html

echo 'if the html files are generated, you can see them raw in httpfiles folder'
echo 'or in the browser localhost/users.html [errors.html],ctrl+C to close server'

cd ./httpfiles; python3 -m http.server
