import os
import sqlite3
from misc.database_actions import database_actions

class sqlite:
    def __init__(self):
        self.connection = sqlite3.connect(os.environ.get('database_name'))
        self.cursor = self.connection.cursor()
        self.create_default()
        self.connection.commit()       
        self.connection.close()
    
    def create_default(self):
        database_actions.create_table_validation(self.cursor,'config','(name TEXT NOT NULL, value TEXT NOT NULL, PRIMARY KEY(name))')
        data = [
            ('time_notification_limit','300'),
            ('notification_destination','logging'),
            ('cpu_overload_counter_limit','30'),
            ('cpu_percent_limit','90'),
            ('cpu_overload_message','CPU com utilizacao acima de {}%'),
            ('memory_overload_counter_limit','30'),
            ('memory_percent_limit','90'),
            ('memory_overload_message','Memoria com utilizacao acima de {}%'),
            ('disk_overload_counter_limit','30'),
            ('disk_percent_limit','90'),
            ('monitored_disk_location','/'),
            ('disk_overload_message','Disco com utilizacao acima de {}%'),
            ('rabbit_host','localhost'),
            ('rabbit_queue','zeus'),
            ('thread_sleep_time','0.6')
        ]
        
        database_actions.insert_validation(self.cursor,'config',"('name','value')",data)
