file = open("spider.txt")
print(file.readline())
print(file.readline())

print(file.read())

file.close()
#si se te olvida cerrar:
with open("spider.txt") as file:
    print(file.readline())

with open("spider.txt") as file:
    for line in file:
        print(line.upper())
#se generan demasiados \n
with open ("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()#ordena alfabetic
print(lines)#plotea \n ó \t

# how to write, 'r' es el default, en general usa 'a' append
with open("novel.txt", "w") as file:
    file.write("It was dark as a cave")
#write returns nº of characters writen

#remove
import os
os.remove('novel.txt')
os.rename("first_draft.txt", "finished_masterpiece.txt")
os.path.exists("novel.txt")#devuelve True
os.path.exists("novel*")#no funciona wildcard
#check cuando se cambio un archivo
os.path.getmtime("novel.txt")#devuelve timestamp
import datetime
timestamp = os.path.getmtime("novel.txt")
datetime.datetime.fromtimestamp(timestamp)
>>> os.path.abspath("novel.txt")
#devuelve->'/home/profesional/Apuntes/googlePython/novel.txt'

#directories
os.getcwd() #devuelve un texto
os.mkdir("newdir")
os.chdir("newdir")#cd
os.mkdir("newnewdir")
os.rmdir("newnewdir")#remueve si está vacio

#code para diferenciar directorio ó archivo
#!/usr/bin/env p´ython3
import os
dir = os.getcwd()
for name in os.listdir(dir):
    fullname = os.path.join(dir,name)
    if os.path.isdir(fullname):
        print("{} es un directorio" .format(fullname))
    else:
        print("{} es un archivo" .format(fullname))
#POR USAR os.path.join() hace que funcione para todos los OS!
# si quiero saber más -> https://docs.python.org/3/library/os.html

##ejercicio de examencillo
import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, 'w') as file:
    pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  timestamp = datetime.datetime.fromtimestamp(timestamp)

  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  return ("{}".format(timestamp.strftime("%Y-%m-%d")))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd

#CSV MODULE
import csv
f = open("/snap/core18/2566/usr/share/distro-info/debian.csv")
csv_f = csv.reader(f)
for row in csv_f:
#se puede hacer: for row in list(csv_f)[1:]: #pa cargarse 1a columna con etiquetas
    version,codename,series,created,release,eol = row
    print("ver:{},codename:{}, series:{}, created:{}, release:{},eol:{}".format(version,codename,series,created,release,eol))
 #hacer csvs
 hosts = [['workstation', '192.168.25.46'], ['webservercloud', '10.2.5.6']]
 with open('hosts.csv', 'w') as hosts_csv:
     writer = csv.writer(hosts_csv)
     writer.writerows(hosts)
#reading & writing with diccionaries
with open('/snap/core18/2566/usr/share/distro-info/debian.csv','r') as f:
    reader = csv.DictReader(f)
    for rows in reader:
        #cada row es un diccionario por fila
#se puede hacer: for row in list(rows)[1:]:
        print('{} codename {} version'.format(rows['codename'], rows['version']))
#el anterior no da error si se queda un campo vacio. Ahora writing:
users = [{'name':'sol', 'username':'x69solx'},{'name':'luna', 'username':'x69lunax'}]
keys = ['name', 'username']
with open('userUsername.csv','w') as file:
    writer = csv.DictWriter(file, fieldnames = keys)
    writer.writeheader()
    writer.writerows(users)#keys = dictionario
