import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Fruit_selling",
    user="postgres",
    password="123"
)

cur = conn.cursor()


conn.commit()
cur.close()
conn.close()


def add_fruit(name, price, stock_quantity):
    cur.execute("INSERT INTO fruits (name, price, stock_quantity) VALUES (%s, %s, %s)",
                (name, price, stock_quantity))
    conn.commit()

def get_all_fruits():
    cur.execute("SELECT * FROM fruits")
    return cur.fetchall()

def add_order(customer_id, order_date, total_amount):
    cur.execute("INSERT INTO orders (customer_id, order_date, total_amount) VALUES (%s, %s, %s)",
                (customer_id, order_date, total_amount))
    conn.commit()

def get_all_orders():
    cur.execute("SELECT * FROM orders")
    return cur.fetchall()

def add_customer(name, email):
    cur.execute("INSERT INTO customers (name, email) VALUES (%s, %s)",
                (name, email))
    conn.commit()

def get_all_customers():
    cur.execute("SELECT * FROM customers")
    return cur.fetchall()

def add_order_item(order_id, fruit_id, quantity, subtotal):
    cur.execute("INSERT INTO order_items (order_id, fruit_id, quantity, subtotal) VALUES (%s, %s, %s, %s)",
                (order_id, fruit_id, quantity, subtotal))
    conn.commit()

def get_order_items_by_order(order_id):
    cur.execute("SELECT * FROM order_items WHERE order_id = %s", (order_id,))
    return cur.fetchall()