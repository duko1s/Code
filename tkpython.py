import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import dbtask


def CreateCustomers():
    print('accepted')
    
def Dismissal():
    print('dismissed')

def CreateEmployee():
    print('arranged')

def ChangePrice():
    print('changed')

def CreateService():
    print('added')

def CreateOrder():
    print('created')
 
 
def create_Employee_window():
    #Создает новое окно с таблицей.
    table_window = tk.Toplevel()
    table_window.title("Таблица")
    
    cursor = dbtask.connect()

    #Вариант 1: Используем Listbox
    listbox = tk.Listbox(table_window, width=40, height=10)
    listbox.pack()
    Employees = dbtask.GetEmployees(cursor)
    for row in Employees:
        Name= row[0]
        Surname= row[1]
        Phone= row[2]
        
        listbox.insert(tk.END, f"{Name}|{Surname}|{Phone}")

    table_window.mainloop()

def create_Customer_window():
    #Создает новое окно с таблицей.
    table_window = tk.Toplevel()
    table_window.title("Таблица")
    
    cursor = dbtask.connect()

    #Вариант 1: Используем Listbox
    listbox = tk.Listbox(table_window, width=40, height=10)
    listbox.pack()
    Customers = dbtask.GetCustomers(cursor)
    for row in Customers:
        Name= row[0]
        Surname= row[1]
        Phone= row[2]
        
        listbox.insert(tk.END, f"{Name}|{Surname}|{Phone}")

    table_window.mainloop()

def create_Service_window():
    #Создает новое окно с таблицей.
    table_window = tk.Toplevel()
    table_window.title("Таблица")
    
    cursor = dbtask.connect()

    #Вариант 1: Используем Listbox
    listbox = tk.Listbox(table_window, width=40, height=10)
    listbox.pack()
    Services = dbtask.GetServices(cursor)
    for row in Services:
        Name= row[0]
        Price= row[1]
        
        
        listbox.insert(tk.END, f"{Name}|{Price}")

    table_window.mainloop()

def create_Order_window():
    #Создает новое окно с таблицей.
    table_window = tk.Toplevel()
    table_window.title("Таблица")
    
    cursor = dbtask.connect()

    #Вариант 1: Используем Listbox
    listbox = tk.Listbox(table_window, width=40, height=10)
    listbox.pack()
    Orders = dbtask.GetOrders(cursor)
    for row in Orders:

        Date= row[0]
        Service= row[1]
        Address= row[2]
        Employee= row[3]
        Customer= row[4]
        

        listbox.insert(tk.END, f"{Date}|{Address}|{Service}|{Employee}|{Customer}")

    table_window.mainloop()


# Создаем главное окно
root = tk.Tk()
root.title("Главное окно")
root.geometry("250x200")

# Кнопка для открытия окна с таблицей
button1 = ttk.Button(root, text="Customers", command=create_Customer_window)
button1.grid(row=0, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

button2 = ttk.Button(root, text="Employees", command=create_Employee_window)
button2.grid(row=1, column=1, ipadx=6,  ipady=6, padx=5, pady=5)

button3 = ttk.Button(root, text="Services", command=create_Service_window)
button3.grid(row=1, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

button4 = ttk.Button(root, text="Orders", command=create_Order_window)
button4.grid(row=0, column=1, ipadx=6,  ipady=6, padx=5, pady=5)


root.mainloop()
