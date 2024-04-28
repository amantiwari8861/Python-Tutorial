import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

def connect_to_database():
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="pdbc"
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Connection to MySQL database closed")

def insert_data():
    name = name_entry.get()
    age = age_entry.get()
    try:
        # Connect to the database
        connection = connect_to_database()

        # Create a cursor object
        cursor = connection.cursor()

        # Execute SQL query to insert data into the table
        query = "INSERT INTO students (name, age) VALUES (%s, %s)"
        cursor.execute(query, (name, age))

        # Commit the transaction
        connection.commit()
        print("Data inserted successfully!")

        # Show success message
        messagebox.showinfo("Success", "Data inserted successfully!")
    except Exception as e:
        print("Error:", e)
        # Show error message
        messagebox.showerror("Error", f"Failed to insert data: {e}")
    finally:
        if connection:
            # Close the connection
            close_connection(connection)
            clear_entries()

def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

def display_all_data():
    try:
        # Connect to the database
        connection = connect_to_database()

        # Create a cursor object
        cursor = connection.cursor()

        # Execute SQL query to fetch all data from the table
        query = "SELECT * FROM students"
        cursor.execute(query)

        # Create a new window to display all data
        display_window = tk.Toplevel(root)
        display_window.title("All Students Data")

        # Create a treeview widget to display data in a table format
        tree = ttk.Treeview(display_window, columns=("Name", "Age"))
        tree.heading("#0", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Age", text="Age")

        # Insert data into the treeview
        for row in cursor:
            tree.insert("", "end", text=row[0], values=(row[1], row[2]))

        tree.pack(expand=True, fill="both")
    except Exception as e:
        print("Error:", e)
        messagebox.showerror("Error", f"Failed to fetch data: {e}")
    finally:
        if connection:
            # Close the connection
            close_connection(connection)

# Create the main window
root = tk.Tk()
root.title("CRUD Application")

# Create labels and entry fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=5, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=5, pady=5)

# Create buttons
insert_button = tk.Button(root, text="Insert", command=insert_data)
insert_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

display_button = tk.Button(root, text="Display All Data", command=display_all_data)
display_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
