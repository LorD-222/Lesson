from tkinter import *  
  
  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')  
menu = Menu(window)  
new_item = Menu(menu)  
new_item.add_command(label='Новый')  
new_item.add_separator()  
new_item.add_command(label='Изменить')  
menu.add_cascade(label='Файл', menu=new_item)  
window.config(menu=menu)  
window.mainloop()