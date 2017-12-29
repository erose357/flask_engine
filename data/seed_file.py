import os
import psycopg2

conn = psycopg2.connect(os.getenv('DATABASE_URL'))

merchants_file = open('./data/merchants.csv')
customers_file = open('./data/customers.csv')
items_file = open('./data/items.csv')
invoices_file = open('./data/invoices.csv')
transactions_file = open('./data/transactions.csv')
invoice_items_file = open('./data/invoice_items.csv')
sql_statement = "COPY %s FROM STDIN DELIMITER ',' CSV HEADER"

def process_file(conn, table_name, file_object):
    cur = conn.cursor()
    cur.copy_expert(sql=sql_statement % table_name, file=file_object)
    conn.commit()
    cur.close()

try:
    process_file(conn,'merchants', merchants_file)
    print('merchants table seeded')
    process_file(conn, 'customers', customers_file)
    print('customers table seeded')
    process_file(conn, 'items', items_file)
    print('items table seeded')
    process_file(conn, 'invoices', invoices_file)
    print('invoices table seeded')
    process_file(conn, 'transactions', transactions_file)
    print('transactions table seeded')
    process_file(conn, 'invoice_items', invoice_items_file)
    print('invoice_items table seeded')
finally:
    conn.close()
