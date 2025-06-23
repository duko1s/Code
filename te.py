import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import dbtask

def create_Employee_window():
    #Создает новое окно с таблицей.
    table_window = tk.Toplevel()
    table_window.title("Таблица")
    
    cursor = dbtask.connect()

    #Вариант 1: Используем Listbox
    # listbox = tk.Listbox(table_window, width=40, height=10)
    # listbox.pack()
    Employees = dbtask.GetEmployees(cursor)
    row = 0
    listStringVar = []
    for item in Employees:
        print(item)
        listStringVar.append((tk.StringVar(value = item[0]), tk.StringVar(value = item[1]), tk.StringVar(value = item[2])))

        # Name=
        # Surname=
        # Phone=

        print(listStringVar)
        
        fildName = ttk.Entry(table_window, textvariable=listStringVar[-1][0])
        fildName.grid(row=row, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

        fildSurname = ttk.Entry(table_window, textvariable=listStringVar[-1][1])
        fildSurname.grid(row=row, column=1, ipadx=6,  ipady=6, padx=5, pady=5)

        fildPhone = ttk.Entry(table_window, textvariable=listStringVar[-1][2])
        fildPhone.grid(row=row, column=2, ipadx=6,  ipady=6, padx=5, pady=5)
        

        btn1 = ttk.Button(table_window, text="edit")
        btn1.grid(row=row, column=3, ipadx=6,  ipady=6, padx=5, pady=5)

        row += 1

    table_window.mainloop()

def create_Customer_window():
    #Создает новое окно с таблицей.
    table_window = tk.Toplevel()
    table_window.title("Таблица")
    
    cursor = dbtask.connect()

    #Вариант 1: Используем Listbox
    # listbox = tk.Listbox(table_window, width=40, height=10)
    # listbox.pack()
    Customers = dbtask.GetCustomers(cursor)
    row = 0
    listStringVar = []
    for item in Customers:
        print(item)
        listStringVar.append((tk.StringVar(value = item[0]), tk.StringVar(value = item[1]), tk.StringVar(value = item[2])))
        # Name = 
        # Surname = 
        # Phone  = 

        print(listStringVar)
        
        fildName = ttk.Entry(table_window, textvariable=listStringVar[-1][0])
        fildName.grid(row=row, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

        fildSurname = ttk.Entry(table_window, textvariable=listStringVar[-1][1])
        fildSurname.grid(row=row, column=1, ipadx=6,  ipady=6, padx=5, pady=5)

        fildPhone = ttk.Entry(table_window, textvariable=listStringVar[-1][2])
        fildPhone.grid(row=row, column=2, ipadx=6,  ipady=6, padx=5, pady=5)
        row += 1

        # listbox.insert(tk.END, f"{Name}|{Surname}|{Phone}")

    table_window.mainloop()

def create_Service_window():
    #Создает новое окно с таблицей.
    table_window = tk.Toplevel()
    table_window.title("Таблица")
    
    cursor = dbtask.connect()

    # #Вариант 1: Используем Listbox
    # listbox = tk.Listbox(table_window, width=40, height=10)
    # listbox.pack()
    Services = dbtask.GetServices(cursor)
    row = 0
    listStringVar = []
    for item in Services:
        print(item)
        listStringVar.append((tk.StringVar(value = item[0]), tk.StringVar(value = item[1])))
        
        # Name=
        # Price=

        print(listStringVar)
        
        
        fildName = ttk.Entry(table_window, textvariable=listStringVar[-1][0])
        fildName.grid(row=row, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

        fildPrice = ttk.Entry(table_window, textvariable=listStringVar[-1][1])
        fildPrice.grid(row=row, column=1, ipadx=6,  ipady=6, padx=5, pady=5)
        row += 1

    table_window.mainloop()

def create_Order_window():
    #Создает новое окно с таблицей.
    table_window = tk.Toplevel()
    table_window.title("Таблица")
    
    cursor = dbtask.connect()

    

    # #Вариант 1: Используем Listbox
    # listbox = tk.Listbox(table_window, width=40, height=10)
    # listbox.pack()
    Orders = dbtask.GetOrders(cursor)
    row = 0
    listStringVar = []
    for item in Orders:
        print(item)
        listStringVar.append((tk.StringVar(value = item[0]), tk.StringVar(value = item[1]), tk.StringVar(value = item[2]), tk.StringVar(value = item[3]), tk.StringVar(value = item[4])))

        # Date= 
        # Service= 
        # Address= 
        # Employee= 
        # Customer= 
        
        print(listStringVar)

        fildDate = ttk.Entry(table_window, textvariable=listStringVar[-1][0])
        fildDate.grid(row=row, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

        fildAddress = ttk.Entry(table_window, textvariable=listStringVar[-1][1])
        fildAddress.grid(row=row, column=2, ipadx=6,  ipady=6, padx=5, pady=5)

        fildService = ttk.Entry(table_window, textvariable=listStringVar[-1][2])
        fildService.grid(row=row, column=3, ipadx=6,  ipady=6, padx=5, pady=5)

        fildEmployee = ttk.Entry(table_window, textvariable=listStringVar[-1][3])
        fildEmployee.grid(row=row, column=4, ipadx=6,  ipady=6, padx=5, pady=5)

        fildCustomer = ttk.Entry(table_window, textvariable=listStringVar[-1][4])
        fildCustomer.grid(row=row, column=5, ipadx=6,  ipady=6, padx=5, pady=5)
        row += 1

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
