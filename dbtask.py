import psycopg2
from psycopg2 import extensions
#Klim_Trade
#postgres
#wer23yu9
def connect() -> extensions.connection:
    conn = psycopg2.connect(host='localhost', 
    user='postgres', 
    password='wer23yu9', 
    dbname='Klim_Trade')
    return conn


def AddCustomer(custName, custSurname, custPhone):
    connector = connect()
    cursor = connector.cursor()
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
    cursor.close()
    connector.close()

def Dismissal(ID):
    connector = connect()
    cursor = connector.cursor()
    try:
        cursor.execute(f"""
                UPDATE Employees SET Status = false
                WHERE EmployeeID = {str(ID)};
                """)
        connector.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connector.close()

def AddEmployee(emplName, emplSurname, emplPhone):
    connector = connect()
    cursor = connector.cursor()
    cursor.execute(f"""
                SELECT * FROM Employees 
                WHERE EmployeeName = '{emplName}' AND
                SurName = '{emplSurname}' AND Phone = '{emplPhone}';
                """)
    count = cursor.rowcount
    if count != 0:
        cursor.execute(f"""
                UPDATE Employees SET Status = TRUE
                WHERE EmployeeName = '{emplName}'
                AND SurName = '{emplSurname}' AND Phone='{emplPhone}';
                """)
        connector.commit()
    else:
        cursor.execute(f"""
                INSERT INTO Employees
                (EmployeeName, SurName, Phone) 
                VALUES 
                ('{emplName}', '{emplSurname}', '{emplPhone}');
                """)
        connector.commit()
    cursor.close()
    connector.close()

def ChangePrice(servName, servPrice):
    connector = connect()
    cursor = connector.cursor()
    try:
        cursor.execute(f"""
                UPDATE Services SET Price = {servPrice} WHERE ServiceName = {servName};
                """)
    except Exception as e:
        print(e)

def AddService(servName, servPrice):
    connector = connect()
    cursor = connector.cursor()
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

def AddOrder(custName, custSurname, custPhone, orderDate, service, address, employee, customer):
    connector = connect()
    cursor = connector.cursor()
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
        AddCustomer(cursor, custName, custSurname, custPhone)
    cursor.close()
    connector.close()

def GetEmployees(cursor):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"""SELECT EmployeeName, Surname, Phone, EmployeeID FROM Employees WHERE Status = TRUE;""")
    results = cursor.fetchall()
    return results

def GetCustomers(cursor):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"""SELECT CustomerName, Surname, Phone FROM Customers;""")
    results = cursor.fetchall()
    return results

def GetServices(cursor):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"""SELECT ServiceName, Price FROM Services;""")
    results = cursor.fetchall()
    return results
        
def GetOrders(cursor):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"""SELECT OrderDate, Service, Address, Employee, Customer FROM Orders;""")
    results = cursor.fetchall()
    return results

if __name__ == "__main__":
    print("Start")
    conn = connect()
    # results = GetEmployees(cursor)
    # for row in results:
    #     EmployeeName= row[0]
    #     EmployeeSurname= row[1]
    #     EmployeePhone= row[2]
    #     EmployeeID= row[3]

    #     print(f"{EmployeeName} {EmployeeSurname} {EmployeePhone} {EmployeeID}")

    # Dismissal(1)
    AddEmployee("Клим", "Минеев", "67772223")
    #Dismissal(5)


    
