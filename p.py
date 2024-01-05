import mysql.connector

con = mysql.connector.connect(host="localhost", user="admin", password="Password@123", database="python_calc")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print("Please select the option -\n" + "1. Add \n" + "2. Sub \n" + "3. Mul \n" + "4. Div")

select = int(input("Select an option from 1, 2, 3, 4: "))
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result = []
operation = []

if select == 1:
    result = add(a, b)
    operation = '+'
elif select == 2:
    result = sub(a, b)
    operation = '-'
elif select == 3:
    result = mul(a, b)
    operation = '*'
elif select == 4:
    result = div(a, b)
    operation = '/'


if (result != 0) & (operation != 0):
    cursor = con.cursor()
    sql = "INSERT INTO datas (operand_1, operation, operand_2, result) VALUES (%s, %s, %s, %s)"
    values = (a, operation, b, result)
    cursor.execute(sql, values)
    con.commit()
    
    print(f"Result of {a} {operation} {b} = {result}")
    print("Record inserted successfully!")

    cursor.close()
    con.close()
else:
    print("Invalid input")
    