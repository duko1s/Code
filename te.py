import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import dbtask

def dismissal(id):
    print("вызов запроса с аргументом ", id)

def add_new_Order_window():
    add_window = tk.Toplevel()
    add_window.title("Добавить заказ")
            
    fildDate = ttk.Entry(add_window)
    fildDate.grid(row=0, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

    fildService = ttk.Entry(add_window)
    fildService.grid(row=0, column=1, ipadx=6,  ipady=6, padx=5, pady=5)
        

    btn1 = ttk.Button(add_window, text="Добавить", command = lambda: dismissal(fildDate.get()))
    btn1.grid(row=0, column=4, ipadx=6,  ipady=6, padx=5, pady=5)

    add_window.mainloop()

def add_new_Customer_window():
    add_window = tk.Toplevel()
    add_window.title("Добавить заказчика")

    label = ttk.Label(add_window, text="Имя")
    label.grid(row=0, column=0, ipadx=6,  ipady=2, padx=5, pady=2)

    label = ttk.Label(add_window, text="Фамилия")
    label.grid(row=0, column=1, ipadx=6,  ipady=2, padx=5, pady=2)

    label = ttk.Label(add_window, text="Телефон")
    label.grid(row=0, column=2, ipadx=6,  ipady=2, padx=5, pady=2)


    fildName = ttk.Entry(add_window)
    fildName.grid(row=1, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

    fildSurname = ttk.Entry(add_window)
    fildSurname.grid(row=1, column=1, ipadx=6,  ipady=6, padx=5, pady=5)

    fildPhone = ttk.Entry(add_window)
    fildPhone.grid(row=1, column=2, ipadx=6,  ipady=6, padx=5, pady=5)
        

    btn1 = ttk.Button(add_window, text="Добавить", command = lambda: dbtask.AddCustomer(fildName.get(), fildSurname.get(), fildPhone.get()))
    btn1.grid(row=1, column=3, ipadx=6,  ipady=6, padx=5, pady=5)

    add_window.mainloop()

def add_new_Service_window():
    add_window = tk.Toplevel()
    add_window.title("Добавить услугу")

    label = ttk.Label(add_window, text="Название")
    label.grid(row=0, column=0, ipadx=6,  ipady=2, padx=5, pady=2)

    label = ttk.Label(add_window, text="Цена")
    label.grid(row=0, column=1, ipadx=6,  ipady=2, padx=5, pady=2)

            
    fildName = ttk.Entry(add_window)
    fildName.grid(row=1, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

    fildPrice = ttk.Entry(add_window)
    fildPrice.grid(row=1, column=1, ipadx=6,  ipady=6, padx=5, pady=5)
        
    
    btn1 = ttk.Button(add_window, text="Добавить", command = lambda: dbtask.AddService(fildName.get(), str(fildPrice.get())))
    btn1.grid(row=1, column=4, ipadx=6,  ipady=6, padx=5, pady=5)

    add_window.mainloop()

def add_new_Employee_window():
    add_window = tk.Toplevel()
    add_window.title("Добавить сотрудника")

    label = ttk.Label(add_window, text="Имя")
    label.grid(row=0, column=0, ipadx=6,  ipady=2, padx=5, pady=2)

    label = ttk.Label(add_window, text="Фамилия")
    label.grid(row=0, column=1, ipadx=6,  ipady=2, padx=5, pady=2)

    label = ttk.Label(add_window, text="Телефон")
    label.grid(row=0, column=2, ipadx=6,  ipady=2, padx=5, pady=2)

            
    fildName = ttk.Entry(add_window)
    fildName.grid(row=1, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

    fildSurname = ttk.Entry(add_window)
    fildSurname.grid(row=1, column=1, ipadx=6,  ipady=6, padx=5, pady=5)

    fildPhone = ttk.Entry(add_window)
    fildPhone.grid(row=1, column=2, ipadx=6,  ipady=6, padx=5, pady=5)
        

    btn1 = ttk.Button(add_window, text="Добавить", command = lambda: dbtask.AddEmployee(fildName.get(), fildSurname.get(), str(fildPhone.get())))
    btn1.grid(row=1, column=4, ipadx=6,  ipady=6, padx=5, pady=5)

    add_window.mainloop()


def create_Employee_window():
    #Создает новое окно с таблицей.
    table_window = tk.Toplevel()
    table_window.title("Сотрудники")
    
    cursor = dbtask.connect()

    #Вариант 1: Используем Listbox
    # listbox = tk.Listbox(table_window, width=40, height=10)
    # listbox.pack()
    Employees = dbtask.GetEmployees(cursor)
    row = 1
    listStringVar = []


    label = ttk.Label(table_window, text="Имя")
    label.grid(row=0, column=0, ipadx=6,  ipady=2, padx=5, pady=2)

    label = ttk.Label(table_window, text="Фамилия")
    label.grid(row=0, column=1, ipadx=6,  ipady=2, padx=5, pady=2)

    label = ttk.Label(table_window, text="Телефон")
    label.grid(row=0, column=2, ipadx=6,  ipady=2, padx=5, pady=2)


    for item in Employees:
        # print(item)
        listStringVar.append((tk.StringVar(value = item[0]), tk.StringVar(value = item[1]), tk.StringVar(value = item[2]), tk.StringVar(value = item[3])))

        # Name=
        # Surname=
        # Phone=

        # print(listStringVar)
        
        fildName = ttk.Entry(table_window, textvariable=listStringVar[-1][0])
        fildName.grid(row=row, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

        fildSurname = ttk.Entry(table_window, textvariable=listStringVar[-1][1])
        fildSurname.grid(row=row, column=1, ipadx=6,  ipady=6, padx=5, pady=5)

        fildPhone = ttk.Entry(table_window, textvariable=listStringVar[-1][2])
        fildPhone.grid(row=row, column=2, ipadx=6,  ipady=6, padx=5, pady=5)
        

        btn1 = ttk.Button(table_window, text="Уволить", command = lambda: dbtask.EmplDismissal(listStringVar[-1][3].get()))
        btn1.grid(row=row, column=4, ipadx=6,  ipady=6, padx=5, pady=5)

        row += 1

    btn2 = ttk.Button(table_window, text="Добавить", command = add_new_Employee_window)
    btn2.grid(row=row, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

    table_window.mainloop()

def create_Customer_window():
    #Создает новое окно с таблицей.
    table_window = tk.Toplevel()
    table_window.title("Заказчики")
    
    cursor = dbtask.connect()

    #Вариант 1: Используем Listbox
    # listbox = tk.Listbox(table_window, width=40, height=10)
    # listbox.pack()
    Customers = dbtask.GetCustomers(cursor)
    row = 1
    listStringVar = []


    label = ttk.Label(table_window, text="Имя")
    label.grid(row=0, column=0, ipadx=6,  ipady=2, padx=5, pady=2)

    label = ttk.Label(table_window, text="Фамилия")
    label.grid(row=0, column=1, ipadx=6,  ipady=2, padx=5, pady=2)

    label = ttk.Label(table_window, text="Телефон")
    label.grid(row=0, column=2, ipadx=6,  ipady=2, padx=5, pady=2)


    for item in Customers:
        # print(item)
        listStringVar.append((tk.StringVar(value = item[0]), tk.StringVar(value = item[1]), tk.StringVar(value = item[2]), tk.StringVar(value = item[3])))
        # Name = 
        # Surname = 
        # Phone  = 

        # print(listStringVar)
        
        fildName = ttk.Entry(table_window, textvariable=listStringVar[-1][0])
        fildName.grid(row=row, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

        fildSurname = ttk.Entry(table_window, textvariable=listStringVar[-1][1])
        fildSurname.grid(row=row, column=1, ipadx=6,  ipady=6, padx=5, pady=5)

        fildPhone = ttk.Entry(table_window, textvariable=listStringVar[-1][2])
        fildPhone.grid(row=row, column=2, ipadx=6,  ipady=6, padx=5, pady=5)

        btn1 = ttk.Button(table_window, text="Удалить", command = lambda: dbtask.CustRemove(listStringVar[-1][3].get()))
        btn1.grid(row=row, column=4, ipadx=6,  ipady=6, padx=5, pady=5)

        row += 1

    btn2 = ttk.Button(table_window, text="Добавить", command = add_new_Customer_window)
    btn2.grid(row=row, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

    table_window.mainloop()

def create_Service_window():
    #Создает новое окно с таблицей.
    table_window = tk.Toplevel()
    table_window.title("Услуги")
    
    cursor = dbtask.connect()

    # #Вариант 1: Используем Listbox
    # listbox = tk.Listbox(table_window, width=40, height=10)
    # listbox.pack()
    Services = dbtask.GetServices(cursor)
    row = 1
    listStringVar = []


    label = ttk.Label(table_window, text="Название")
    label.grid(row=0, column=0, ipadx=6,  ipady=2, padx=5, pady=2)

    label = ttk.Label(table_window, text="Цена")
    label.grid(row=0, column=1, ipadx=6,  ipady=2, padx=5, pady=2)


    for item in Services:
        # print(item)
        listStringVar.append((tk.StringVar(value = item[0]), tk.StringVar(value = item[1]), tk.StringVar(value = item[2])))
        
        # Name=
        # Price=

        # print(listStringVar)
        
        
        fildName = ttk.Entry(table_window, textvariable=listStringVar[-1][0])
        fildName.grid(row=row, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

        fildPrice = ttk.Entry(table_window, textvariable=listStringVar[-1][1])
        fildPrice.grid(row=row, column=1, ipadx=6,  ipady=6, padx=5, pady=5)

        btn1 = ttk.Button(table_window, text="Удалить", command = lambda: dbtask.ServRemove(listStringVar[-1][2].get()))
        btn1.grid(row=row, column=4, ipadx=6,  ipady=6, padx=5, pady=5)

        row += 1

    btn2 = ttk.Button(table_window, text="Добавить", command = add_new_Service_window)
    btn2.grid(row=row, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

    table_window.mainloop()

def create_Order_window():
    #Создает новое окно с таблицей.
    table_window = tk.Toplevel()
    table_window.title("Заказы")
    
    cursor = dbtask.connect()

    

    # #Вариант 1: Используем Listbox
    # listbox = tk.Listbox(table_window, width=40, height=10)
    # listbox.pack()
    Orders = dbtask.GetOrders(cursor)
    row = 1
    listStringVar = []


    label = ttk.Label(table_window, text="Дата")
    label.grid(row=0, column=0, ipadx=6,  ipady=2, padx=5, pady=2)

    label = ttk.Label(table_window, text="Адресс")
    label.grid(row=0, column=1, ipadx=6,  ipady=2, padx=5, pady=2)

    label = ttk.Label(table_window, text="Услуга")
    label.grid(row=0, column=2, ipadx=6,  ipady=2, padx=5, pady=2)

    label = ttk.Label(table_window, text="Сотрудник")
    label.grid(row=0, column=3, ipadx=6,  ipady=2, padx=5, pady=2)

    label = ttk.Label(table_window, text="Заказчик")
    label.grid(row=0, column=4, ipadx=6,  ipady=2, padx=5, pady=2)


    for item in Orders:
        # print(item)
        listStringVar.append((tk.StringVar(value = item[0]), tk.StringVar(value = item[1]), tk.StringVar(value = item[2]), tk.StringVar(value = item[3]), tk.StringVar(value = item[4]), tk.StringVar(value = item[5])))


        # Date= 
        # Service= 
        # Address= 
        # Employee= 
        # Customer= 
        
        # print(listStringVar)

        fildDate = ttk.Entry(table_window, textvariable=listStringVar[-1][0])
        fildDate.grid(row=row, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

        fildAddress = ttk.Entry(table_window, textvariable=listStringVar[-1][2])
        fildAddress.grid(row=row, column=1, ipadx=6,  ipady=6, padx=5, pady=5)

        fildService = ttk.Entry(table_window, textvariable=listStringVar[-1][1])
        fildService.grid(row=row, column=2, ipadx=6,  ipady=6, padx=5, pady=5)

        fildEmployee = ttk.Entry(table_window, textvariable=listStringVar[-1][3])
        fildEmployee.grid(row=row, column=3, ipadx=6,  ipady=6, padx=5, pady=5)

        fildCustomer = ttk.Entry(table_window, textvariable=listStringVar[-1][4])
        fildCustomer.grid(row=row, column=4, ipadx=6,  ipady=6, padx=5, pady=5)

        btn1 = ttk.Button(table_window, text="Удалить", command = lambda: dismissal(listStringVar[-1][5].get()))
        btn1.grid(row=row, column=6, ipadx=5,  ipady=6, padx=5, pady=5)

        row += 1

    btn2 = ttk.Button(table_window, text="Добавить", command = add_new_Order_window)
    btn2.grid(row=row, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

    table_window.mainloop()


# def reopcust():
#     add_new_Customer_window.destroy()
#     create_Customer_window()



# Создаем главное окно
root = tk.Tk()
root.title("Главное окно")
root.geometry("250x200")

# Кнопка для открытия окна с таблицей
button1 = ttk.Button(root, text="Заказчики", command=create_Customer_window)
button1.grid(row=0, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

button2 = ttk.Button(root, text="Сотрудники", command=create_Employee_window)
button2.grid(row=1, column=1, ipadx=6,  ipady=6, padx=5, pady=5)

button3 = ttk.Button(root, text="Услуги", command=create_Service_window)
button3.grid(row=1, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

button4 = ttk.Button(root, text="Заказы", command=create_Order_window)
button4.grid(row=0, column=1, ipadx=6,  ipady=6, padx=5, pady=5)





root.mainloop()
