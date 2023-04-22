import mysql.connector
import tkinter as tk
from tkinter import ttk

# establish database connection
mydb = mysql.connector.connect(
  host="localhost",
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

# create a Tkinter window
root = tk.Tk()
root.title("Data from MySQL")

# create a treeview widget to display the data
tree = ttk.Treeview(root)
tree["columns"] = tuple(range(len(results[0])))
tree["show"] = "headings"
for i in range(len(results[0])):
    tree.heading(i, text="Column "+str(i+1))
tree.pack()

# insert data into the treeview widget
for row in results:
    tree.insert("", "end", values=row)

# start the Tkinter event loop
root.mainloop()

# close the cursor and database connection
mycursor.close()
mydb.close()
