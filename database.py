import psycopg2
#establishing connection to postgres
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='1234',dbname='myduka')
#object to perform database operations.
cur = conn.cursor()
def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products


def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales


def get_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock

