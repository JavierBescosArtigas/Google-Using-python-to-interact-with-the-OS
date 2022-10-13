#!/usr/bin/env python3

#THEORY
#stdin->standard input
#stdout-> standard output
#stderr-> standar error
#exis status: 0 GOOD, $? nos da el último exit value. POdemos usar en python sys.exit(1) para errores
#export en bash crea nueva variable de entorno

#IMPORTACIONES
import os
import sys
import subprocess

#EXERCISES
def exercise1():
    data = input("this will come from STDIN ")
    print("Now we write in STDOUT" + ' ' + data)
    print("now we generate an error to STDERR :" + data +1)

def exercise2():
    print("HOME: " + os.environ.get("HOME", ""))
    print("SHELL: {}" .format(os.environ.get("SHELL","")))
    print("FRUIT: " +os.environ.get("FRUIT","")) #si no pusieramos "", devolveria error, de esta manera decimos que si no devuelva""
#exercise2()

def exercise3():
    print(sys.argv)
#exercise3()

def exercise4(): #empezamos con subprocess
    #subprocess.run(["date"])
    result = subprocess.run(["host","8.8.8.8"], capture_output=True)
    print(result.stdout) #la b indica que recibe bytes
    print(result.stdout.decode().split()) #UTF_8 es codificacion estandar
    result2 = subprocess.run(["rm", "doesnotexists"], capture_output = True)
    print("status code para rm: {}" .format(result2.returncode))
    print("stdout para rm: {}\n stderr: {}" .format(result2.stdout.decode(), result2.stderr.decode()))
#exercise4()

def exercise5(): #cambiaremos las variables de entorno
    my_env = os.environ.copy() #siempre proceder así: copias env, cambias y lo devuelves copy crea un diccionario del 'env'
    my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])
    result = subprocess.run(["myapp"], env=my_env)
