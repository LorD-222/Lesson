import subprocess
import time

def shutdown(name_ws):
   subprocess.call(["shutdown", "-r","-m", "\\\\" + name_ws, "-t", "30"])
   time.sleep(1)
   stop_fun = input("Хотите отменить перезагрузку?y/n")
   if stop_fun == "y":
      subprocess.call(["shutdown", "-a",  "-m", "\\\\" + name_ws])
   else:
      time.sleep(2)


def restart_spooler(name_ws):
   subprocess.call(['sc',"\\\\" + name_ws, 'stop', 'PDF24'])
   time.sleep(3)
   subprocess.call(['sc',"\\\\" + name_ws, 'stop', 'Spooler'])
   subprocess.call(['sc',"\\\\" + name_ws, 'start', 'Spooler'])
   time.sleep(3)
   subprocess.call(['sc',"\\\\" + name_ws, 'start', 'PDF24'])

def stop_service(name_ws, name_service):
   subprocess.call(['sc',"\\\\" + name_ws , 'stop', name_service])
   time.sleep(3)
   
def start_service(name_ws, name_service):
   subprocess.call(['sc',"\\\\" + name_ws , 'start', name_service])
   time.sleep(3) 

