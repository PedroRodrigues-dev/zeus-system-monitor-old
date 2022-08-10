import os
import sqlite3

class database_actions:
    def create_table_validation(cursor, name, columns):
        try:
            cursor.execute(f'CREATE TABLE {name} {columns}')
        except:
            pass
    
    def insert_validation(cursor, table, columns, data):
        model = '?,'*len(columns.split(','))
        try:
            cursor.executemany(f"INSERT INTO {table} {columns} VALUES ({model[:-1]})", data)
        except:
            pass
    
    def find_config_values(name):
        connection = sqlite3.connect(os.environ.get('database_name'))
        cursor = connection.cursor()
        return cursor.execute(f"select value from config where name = '{name}'").fetchone()[0]