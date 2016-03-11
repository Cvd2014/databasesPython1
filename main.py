from database.mysql import MySQLDatabase  # import driver

my_db_connection = MySQLDatabase('test_employees', 'root', 'Ciaran03', 'localhost')


kwargs={"where":"emp_no LIKE '1000%'",
        "limit":"10"
        }
wheres={"emp_no":"= 10001"}

print my_db_connection.select('employees',['first_name', 'last_name', 'emp_no'] ,**kwargs)

my_db_connection.delete('employees', **wheres)

print "\n"
print"New List"

print my_db_connection.select('employees',['first_name', 'last_name', 'emp_no'] ,**kwargs)




