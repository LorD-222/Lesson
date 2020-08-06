import subprocess
import time

def shutdown():
   name_ws = input("Введите имя ПК: ")
   subprocess.call(["shutdown", "-r","-m", name_ws, "-t", "10"])
   
def restart_spooler():
   subprocess.call(['sc', 'stop', 'PDF24'])
   time.sleep(3)
   subprocess.call(['sc', 'stop', 'Spooler'])
   subprocess.call(['sc', 'start', 'Spooler'])
   time.sleep(3)
   subprocess.call(['sc', 'start', 'PDF24'])
       

