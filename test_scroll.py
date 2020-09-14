from tkinter import *  
from tkinter import scrolledtext  

def clicked():  
    txt.delete(1.0, END)  # мы передали координаты очистки   
  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')  
txt = scrolledtext.ScrolledText(window, width=40, height=10)  
txt.grid(column=0, row=0)  
txt.insert(INSERT, 'Текстовое поле')


btn = Button(window, text="Клик", command=clicked)
btn.grid(column=2, row=41)
window.mainloop()