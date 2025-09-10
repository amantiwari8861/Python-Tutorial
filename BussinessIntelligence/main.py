import pymysql
from decimal import Decimal

# 🔹 Establish connection
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="sampledatabase",
)
cursor = conn.cursor()

# 🔹 BI Queries
queries = {
    1: ("Top 5 Customers by Revenue", """
        SELECT c.customerName, SUM(od.quantityOrdered * od.priceEach) AS revenue
        FROM customers c
        JOIN orders o ON c.customerNumber = o.customerNumber
        JOIN orderdetails od ON o.orderNumber = od.orderNumber
        GROUP BY c.customerName
        ORDER BY revenue DESC
        LIMIT 5;
    """),
    2: ("Sales by Country", """
        SELECT c.country, SUM(od.quantityOrdered * od.priceEach) AS total_sales
        FROM customers c
        JOIN orders o ON c.customerNumber = o.customerNumber
        JOIN orderdetails od ON o.orderNumber = od.orderNumber
        GROUP BY c.country
        ORDER BY total_sales DESC
        LIMIT 10;
    """),
    3: ("Monthly Sales Trend", """
        SELECT DATE_FORMAT(o.orderDate, '%Y-%m') AS month,
               SUM(od.quantityOrdered * od.priceEach) AS revenue
        FROM orders o
        JOIN orderdetails od ON o.orderNumber = od.orderNumber
        GROUP BY month
        ORDER BY month;
    """),
    4: ("Product Line Performance", """
        SELECT p.productLine, SUM(od.quantityOrdered * od.priceEach) AS sales
        FROM products p
        JOIN orderdetails od ON p.productCode = od.productCode
        GROUP BY p.productLine
        ORDER BY sales DESC;
    """),
    5: ("Employee Sales Performance", """
        SELECT e.firstName, e.lastName, SUM(od.quantityOrdered * od.priceEach) AS total_sales
        FROM employees e
        JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
        JOIN orders o ON c.customerNumber = o.customerNumber
        JOIN orderdetails od ON o.orderNumber = od.orderNumber
        GROUP BY e.employeeNumber
        ORDER BY total_sales DESC
        LIMIT 5;
    """)
}

def run_query(choice):
    title, sql = queries[choice]
    print(f"\n📊 {title} 📊\n" + "-"*50)
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        # Convert Decimal to float for display
        display_row = tuple(float(x) if isinstance(x, Decimal) else x for x in row)
        print(display_row)

# 🔹 Menu Loop
while True:
    print("\n====== BI Demo Menu ======")
    for key, (title, _) in queries.items():
        print(f"{key}. {title}")
    print("0. Exit")
    
    try:
        choice = int(input("\nEnter your choice: "))
        if choice == 0:
            print("Exiting... ✅")
            break
        elif choice in queries:
            run_query(choice)
        else:
            print("❌ Invalid choice, try again.")
    except ValueError:
        print("❌ Please enter a number.")

cursor.close()
conn.close()
