#IDC
#Luis Roberto Martinez Ramirez A01662619 
#Se hace un registro informativo de una serie de procesos que ejecuta el programa 

import psutil
import json
from datetime import datetime

def get_processes_info():
    processes = []

    for process in psutil.process_iter():

        with process.oneshot():

            pid = process.pid
            if pid == 0:

                continue

            name = process.name()

            try:

                create_time = datetime.fromtimestamp(process.create_time())
                
            except OSError:
              
                create_time = datetime.fromtimestamp(psutil.boot_time())

            try:
                
                cores = len(process.cpu_affinity())
              
            except psutil.AccessDenied:
              
                cores = 0

            cpu_usage = process.cpu_percent()

            status = process.status()
            try:

                nice = int(process.nice())
            except psutil.AccessDenied:
                nice = 0  
            try:
              
                memory_usage = process.memory_full_info().uss
            except psutil.AccessDenied:
                memory_usage = 0
              
            io_counters = process.io_counters()
            read_bytes = io_counters.read_bytes
            write_bytes = io_counters.write_bytes

            n_threads = process.num_threads()
            try:
                username = process.username()
            except psutil.AccessDenied:
                username = "N/A"
            processes.append({
                'pid' : pid, 'name' : name, 'create_time' : str(create_time),
                'cores' : cores, 'cpu_usage' : cpu_usage, 'status' : status, 'nice' : nice,
                'memory_usage' : memory_usage, 'read_bytes' : read_bytes, 'write_bytes' : write_bytes,
                'n_threads' : n_threads, 'username' : username,
            })
    return processes

for p in get_processes_info():
    #print(type(p)) = dict
    #print(p)
    json_str = json.dumps(p)
    print(json_str)

""" 
¿Que es un PCB?
Es un registro de un  proceso en especifico que ejecuta el sistema operativo

¿Para que sirve la libreria psutil en python?
para poder hacer registro de procesos en diferentes plataformas ##(linux, windows, mac, etc)

Resultado del programa
{'pid': 1, 'name': '.pid1-wrapped', 'create_time': datetime.datetime(2022, 9, 28, 16, 30, 36, 120000), 'cores': 6, 'cpu_usage': 0.0, 'status': 'sleeping', 'nice': 0, 'memory_usage': 16666624, 'read_bytes': 16183296, 'write_bytes': 5910528, 'n_threads': 18, 'username': 'runner'}
{'pid': 291, 'name': 'bash', 'create_time': datetime.datetime(2022, 9, 28, 16, 36, 46, 320000), 'cores': 6, 'cpu_usage': 0.0, 'status': 'sleeping', 'nice': 0, 'memory_usage': 1138688, 'read_bytes': 0, 'write_bytes': 0, 'n_threads': 1, 'username': 'runner'}
{'pid': 292, 'name': 'python3.8', 'create_time': datetime.datetime(2022, 9, 28, 16, 36, 46, 520000), 'cores': 6, 'cpu_usage': 0.0, 'status': 'sleeping', 'nice': 0, 'memory_usage': 107163648, 'read_bytes': 49152, 'write_bytes': 7163904, 'n_threads': 2, 'username': 'runner'}
{'pid': 303, 'name': 'python3.8', 'create_time': datetime.datetime(2022, 9, 28, 16, 36, 49, 220000), 'cores': 6, 'cpu_usage': 0.0, 'status': 'sleeping', 'nice': 0, 'memory_usage': 17428480, 'read_bytes': 405504, 'write_bytes': 0, 'n_threads': 1, 'username': 'runner'}
{'pid': 659, 'name': 'ld-linux-x86-64.so.2', 'create_time': datetime.datetime(2022, 9, 28, 16, 40, 38, 390000), 'cores': 6, 'cpu_usage': 0.0, 'status': 'running', 'nice': 0, 'memory_usage': 7122944, 'read_bytes': 0, 'write_bytes': 0, 'n_threads': 6, 'username': 'runner'}
  
¿Qué puedes inferir acerca del ambiente en el que se ejecuta tu programa, a partir de la información obtenida?
se ejecuta en lines en 64 bits y que la hora de la ejecucion ronda entre las 4 y las 5 que puede ser un pais del sureste como Africa y tiene un uso de memeoria de 7gb y no hay escritura de bytes 

"""
       
            
          