import sqlite3
import misc.variables as variables

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
        connection = sqlite3.connect('cfg.sqlite3')
        cursor = connection.cursor()
        return cursor.execute(f"select value from config where name = '{name}'").fetchone()[0]
    
    def find_all_configs():
        connection = sqlite3.connect('cfg.sqlite3')
        cursor = connection.cursor()
        return cursor.execute('select * from config').fetchall()
    
    def find_one_config(name):
        connection = sqlite3.connect('cfg.sqlite3')
        cursor = connection.cursor()
        return cursor.execute(f"select * from config where name = '{name}'").fetchone()
    
    def update_config(name, value):
        connection = sqlite3.connect('cfg.sqlite3')
        cursor = connection.cursor()
        try:
            cursor.execute(f"update config set value = '{value}' where name = '{name}'")
            connection.commit()
            variables.define_monitors_variables = True
            return database_actions.find_one_config(name)
        except:
            return 'Nome ou valor invalido!'