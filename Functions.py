import subprocess
import time

def shutdown():
   name_ws = input("Введите имя ПК: ")
   subprocess.call(["shutdown", "-r","-m", name_ws, "-t", "10"])
   time.sleep(3)

def restart_spooler():
   name_ws = input("Введите имя ПК:")
   subprocess.call(['sc',name_ws, 'stop', 'PDF24'])
   time.sleep(3)
   subprocess.call(['sc',name_ws, 'stop', 'Spooler'])
   subprocess.call(['sc',name_ws, 'start', 'Spooler'])
   time.sleep(3)
   subprocess.call(['sc',name_ws, 'start', 'PDF24'])

def stop_service():
   name_ws = input("Введите имя ПК:")
   name_service = input("Введите имя службы:")
   subprocess.call(['sc',"\\\\" + name_ws , 'stop', name_service])
   time.sleep(3)
   
def start_service():
   name_ws = input("Введите имя ПК:")
   name_service = input("Введите имя службы:")
   subprocess.call(['sc',"\\\\" + name_ws , 'start', name_service])
   time.sleep(3) 

