import psycopg2
from psycopg2 import extensions
#Klim_Trade
#postgres
#wer23yu9
def connect() -> extensions.connection:
    conn = psycopg2.connect(host='192.168.88.51', 
    user='postgres', 
    password='wer23yu9', 
    dbname='Klim_Trade')
    return conn




def EmplDismissal(ID):
    connector = connect()
    cursor = connector.cursor()
    try:
        cursor.execute(f"""
                UPDATE Employees SET Status = false
                WHERE EmployeeID = '{str(ID)}';
                """)
        connector.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connector.close()

def ServRemove(ID):
    connector = connect()
    cursor = connector.cursor()
    try:
        cursor.execute(f"""
                DELETE FROM Services
                WHERE ServiceID = '{ID}';
                """)
        connector.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connector.close()

def CustRemove(ID):
    connector = connect()
    cursor = connector.cursor()
    try:
        cursor.execute(f"""
                DELETE FROM Customers
                WHERE CustomerID = '{ID}';
                """)
        connector.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connector.close()




def AddCustomer(custName, custSurname, custPhone):
    connector = connect()
    cursor = connector.cursor()
    cursor.execute(f"""
            INSERT INTO Customers
            (CustomerName, SurName, Phone) 
            VALUES 
            ('{custName}', '{custSurname}', '{custPhone}');
            """)
    connector.commit()
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
                WHERE ServiceName = '{servName}' AND Price = '{servPrice}';
                """)
    count = cursor.rowcount
    if count == 0:
        cursor.execute(f"""
                INSERT INTO Services
                (ServiceName, Price) 
                VALUES 
                ('{servName}', '{servPrice}');
                """)
        connector.commit()
    cursor.close()
    connector.close()

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
    cursor.execute(f"""SELECT CustomerName, Surname, Phone, CustomerID FROM Customers;""")
    results = cursor.fetchall()
    return results

def GetServices(cursor):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"""SELECT ServiceName, Price, ServiceID FROM Services;""")
    results = cursor.fetchall()
    return results
        
def GetOrders(cursor):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"""SELECT OrderDate, Service, Address, Employee, Customer, OrderID FROM Orders;""")
    results = cursor.fetchall()
    common_results = []
    for result in results:
        date = result[0]
        cursor.execute(f"""SELECT ServiceName FROM Services WHERE ServiceID = {result[1]};""")
        service = cursor.fetchall()[0][0]
        address = result[2]
        cursor.execute(f"""SELECT EmployeeName, Surname FROM Employees WHERE EmployeeID = {result[3]};""")
        e_name, e_surname = cursor.fetchall()[0]
        cursor.execute(f"""SELECT CustomerName, Surname FROM Customers WHERE CustomerID = {result[4]};""")
        c_name, c_surname = cursor.fetchall()[0]
        id = result[5]
        common_results.append((date, service, address, f"{e_name} {e_surname}", f"{c_name} {c_surname}", id))
    return common_results

if __name__ == "__main__":
    print("Start")
    conn = connect()
    print(GetOrders())

    
