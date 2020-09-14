import subprocess
import time
from tkinter import *  
  
#Window  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('800x600')

'''def clicked():
   args = ["ping", "90514-ws911"]
   process = subprocess.Popen(args, stdout=subprocess.PIPE)
   data = process.communicate()
   lbl.configure(text=data)
'''

def clicked():
   res = "Привет {}".format(txt.get())
   lbl.configure(text=res)

#Text
lbl = Label(window, text="Привет", font=("Arial Bold", 10)) 
lbl.grid(column=0, row=0)  

#text box
txt = Entry(window,width=40)  
txt.grid(column=1, row=0) 
txt.focus()
#Button
btn = Button(window, text="Не нажимать!", command=clicked)  
btn.grid(column=2, row=0)






window.mainloop()