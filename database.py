import psycopg2

conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='1234',dbname='myduka')

cur = conn.cursor()


#fetching products
def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products


#fetching sales
def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales


#fetching stock
def get_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock


def get_data(table):
    cur.execute(f"select * from {table}")
    data = cur.fetchall()
    return data