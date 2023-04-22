import mysql.connector

# establish database connection
mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="adminuser",
  database="sql_hr"
)

# create a cursor object to execute queries
mycursor = mydb.cursor()

# execute a SELECT statement
mycursor.execute("SELECT * FROM sql_hr.employees")

# fetch all rows from the result set
results = mycursor.fetchall()

# iterate through the rows and print them
for row in results:
    print(row)
    
# close the cursor and database connection
mycursor.close()
mydb.close()
