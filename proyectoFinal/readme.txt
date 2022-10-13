The proyect consists of reading the log file,
with REGEX obtaining the info needed:
    1) usernames,number_of_errors,number_of_success
    2)errortypes,count
After that, everything is transformed to a html file with csv_to_html.py
    to be able to access it via webpage
    *for example making a http server in the folder with the *.html files
        with python3 -m http.server
--------------------------------
COMANDS TO USE:

./ticky_check.py

mkdir httpfiles

./csv_to_html.py ./errorsTohtml.csv ./httpfiles/errors.html

./csv_to_html.py ./usersTohtml.csv ./httpfiles/users.html

cd ./httpfiles

python3 -m http.server

