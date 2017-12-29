import os
import psycopg2

conn = psycopg2.connect(os.getenv('DATABASE_URL'))

merchants_file = open('./data/merchants.csv')
customers_file = open('./data/customers.csv')
sql_statement = "COPY %s FROM STDIN DELIMITER ',' CSV HEADER"

def process_file(conn, table_name, file_object):
    cur = conn.cursor()
    cur.copy_expert(sql=sql_statement % table_name, file=file_object)
    conn.commit()
    cur.close()

try:
    process_file(conn,'merchants', merchants_file)
    print('Merchants table seeded')
    process_file(conn, 'customers', customers_file)
    print('Customers table seeded')
finally:
    conn.close()
