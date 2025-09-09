import sqlite3
from datetime import datetime
import os
import pandas
class Database:
    def __init__(self, db_name = '../database.db'):
        self.db_name = os.path.abspath(db_name)
        
        
    def create_table(self, table_name, keys = []):
        columns = ','.join(keys)
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name}({columns})')
            connection.commit()
            return
        
    def insert_data(self, table_name, values = []):
        try:
        
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                if table_name == 'products':
                    QUERY = f"""INSERT INTO products (ProductName, Price, SubmissionDate, ProductLink, ProductImage)
                    VALUES (?,?,?,?,?);"""
                    for item in values:
                        cursor.execute(QUERY, (item['product_name'],item['product_price'], datetime.now().strftime('%Y%m%d_%H%M'), item['product_link'], item['product_image']))
                        print(f'Data of {item} added succesfully')
                elif table_name == 'links':
                    QUERY = f"""INSERT INTO links (ProductLink) VALUES (?);"""
                    for item in values: 
                        cursor.execute(QUERY, (item['ProductLink']))
                        print(f'Data of {item} added succesfully')      
                connection.commit()
                return
        except Exception as e:
            return e
        
    def read_data(self, table_name):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()    
            cursor.execute(f'SELECT * FROM {table_name}')
            return cursor.fetchall()
        

    def sql_to_csv(self, table):
        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                clients = pandas.read_sql(f'SELECT * FROM {table}', connection)
                data_path = 'data'
                os.makedirs(data_path, exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M")
                file = os.path.join(data_path, f'{table}_{timestamp}.csv')
                clients.to_csv(file, index=False)
                return file
        except Exception as e:
            return e
        
    def custom_query(self, query):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        
        





