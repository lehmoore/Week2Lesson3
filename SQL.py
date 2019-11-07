import pyodbc

# Variables to connect to DB.
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

docker_northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

# What is a cursor?
cursor = docker_northwind.cursor()
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
print(row)

# We can also Fetch all rows
all_customers = cursor.execute("SELECT * FROM Customers;").fetchall()
# Fetch all is dangerous as it can block out CPU with huge amount of data.

print(all_customers)
print(type(all_customers))

for row in all_customers:
    # do operations with data.
    print(row.ContactName, row.Fax)

# Because this is dangerous we can use a while loop to fetchone()
# until record / row is none --> break.

all_products = cursor.execute("SELECT * FROM Products;")

# This is more efficient than fetchall().
while True:
    row_record = all_products.fetchone()
    if row_record is None:
        break
    print(row_record.UnitPrice)