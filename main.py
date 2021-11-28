import subprocess
import platform
import socket
import time
import os

path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Bienvenido")
while True:
    code = input(">>> ")
    if code == 'ping':
        host = input("Introduce la ip adress ")
        number = input("Indtroduce el tiempo del Ping: ")

        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))
    if code == 'local':
        print("Tu ip  " + host_ip)
        print("Tu local Host: " + host_name)
    if code == 'date':
        print("La fecha actual: " + time.strftime("%m/%d/%Y"))
    if code == 'list':
        dir_list = os.listdir(path)
        print("Ficheros y directorios '", path, "' :")
        print(dir_list)
    if code == 'list -a':
        file = input("Introduce la ruta del Path: ")
        dir_list2 = os.listdir(file)
        print("Ficheros  '", file, "':")
        print(dir_list2)
    if code == 'echo':
        echo = input("Nop ")