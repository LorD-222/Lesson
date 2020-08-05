def shutdown():
   import subprocess
   name_ws = input("Введите имя ПК: ")
   subprocess.call(["shutdown", "-r","-m", name_ws, "-t", "10"])

