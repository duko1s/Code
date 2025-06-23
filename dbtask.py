import psycopg2
#Klim_Trade
#postgres
#wer23yu9
def connect():
    conn = psycopg2.connect(host='localhost', 
    user='postgres', 
    password='wer23yu9', 
    dbname='Klim_Trade')
    return conn.cursor()


def CreateCustomers(cursor, custName, custSurname, custPhone):
    try:
        cursor.execute(f"""
                CREATE TABLE Customers(
        CustomerID SERIAL PRIMARY KEY NOT NULL,
        {custName} varchar (40) NOT NULL,
        {custSurname} varchar (40) NULL,
        {custPhone} char(15) NOT NULL
        );
                """)
    except Exception as e:
        print(e)

def Dismissal(cursor, emplName, emplSurname):
    try:
        cursor.execute(f"""
                UPDATE Employees SET Status = FALSE
                WHERE EmployeeName = {emplName} AND SurName = {emplSurname};
                """)
    except Exception as e:
        print(e)

def CreateEmployee(cursor, emplName, emplSurname, emplPhone):
    cursor.execute(f"""
                SELECT * FROM Employees 
                WHERE EmployeeName = {emplName},
                SurName = {emplSurname}, Phone = {emplPhone};
                """)
    count = cursor.rowcount
    if count != 0:
        cursor.execute(f"""
                UPDATE Employees SET Status = TRUE
                WHERE EmployeeName = {emplName}
                AND SurName = {emplSurname} AND Phone={emplPhone};
                """)
    else:
        cursor.execute(f"""
                INSERT INTO Employees
                (EmployeeName, SurName, Phone) 
                VALUES 
                ({emplName}, {emplSurname}, {emplPhone});
                """)

def ChangePrice(cursor, servName, servPrice):
    try:
        cursor.execute(f"""
                UPDATE Services SET Price = {servPrice} WHERE ServiceName = {servName};
                """)
    except Exception as e:
        print(e)

def CreateService(cursor, servName, servPrice):
    cursor.execute(f"""
                SELECT * FROM Services 
                WHERE ServiceName = {servName}, Price = {servPrice};
                """)
    count = cursor.rowcount
    if count == 0:
        cursor.execute(f"""
                INSERT INTO Services
                (ServiceName, Price) 
                VALUES 
                ({servName}, {servPrice});
                """)

def CreateOrder(cursor, custName, custSurname, custPhone, orderDate, service, address, employee, customer):
    cursor.execute(f"""
                SELECT * FROM Customers
                WHERE CustomerName = {custName},
                SurName = {custSurname}, Phone = {custPhone};
                """)
    count = cursor.rowcount
    if count != 0:
        cursor.execute(f"""
                INSERT INTO Order
                (OrderDate, Service, Address, Employee, Customer) 
                VALUES 
                ({orderDate}, {service}, {address}, {employee}, {customer});
                """)
    else:
        CreateCustomers(cursor, custName, custSurname, custPhone)

def GetEmployees(cursor):
    cursor.execute(f"""SELECT EmployeeName, Surname, Phone FROM Employees WHERE Status = TRUE;""")
    results = cursor.fetchall()
    return results

def GetCustomers(cursor):
    cursor.execute(f"""SELECT CustomerName, Surname, Phone FROM Customers;""")
    results = cursor.fetchall()
    return results

def GetServices(cursor):
    cursor.execute(f"""SELECT ServiceName, Price FROM Services;""")
    results = cursor.fetchall()
    return results
        
def GetOrders(cursor):
    cursor.execute(f"""SELECT OrderDate, Service, Address, Employee, Customer FROM Orders;""")
    results = cursor.fetchall()
    return results

if __name__ == "__main__":
    print("Start")
    cursor = connect()
    results = GetOrders(cursor)
    for row in results:
        Date= row[0]
        Service= row[1]
        Address= row[2]
        Employee= row[3]
        Customer= row[4]
        print(f"{Date} {Service} {Address} {Employee} {Customer} ")


    
