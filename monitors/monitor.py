from time import sleep, time
from misc.database_actions import database_actions
from misc.sending import notification
import psutil
import misc.variables as variables

class monitor:
    def __init__(self, option):
        self.define_variables()
        self.time_last_notification = time()
        self.overload_counter = 0 
        self.monitor_name = self.number_to_name(option)
        self.monitoring(option)
        
    def number_to_name(self, option):
        if option == 0:
            return 'cpu'
        elif option == 1:
            return 'memory'
        else:
            return 'disk'
    
    def switcher(self, option):
        if option == 0:
            percent = psutil.cpu_percent(percpu=True, interval=0.1)
            return sum(percent)/len(percent)
        elif option == 1:
            data = psutil.virtual_memory()
            return 100 - (data.available * 100)/ data.total
        else:
            data = psutil.disk_usage(self.enviroment['monitored_disk_location'])
            return data.percent
    
    def monitoring(self, option):
        while variables.monitors_loop:
            percent_avg = self.switcher(option)
            if percent_avg > int(self.enviroment[f'{self.monitor_name}_percent_limit']):
                    self.overload_counter += 1
            if self.overload_counter > int(self.enviroment[f'{self.monitor_name}_overload_counter_limit']) and (time() - self.time_last_notification) > int(self.enviroment['time_notification_limit']):
                self.time_last_notification = time()
                self.overload_counter = 0
                notification(message=self.enviroment[f'{self.monitor_name}_overload_message'].format(int(self.enviroment[f'{self.monitor_name}_percent_limit'])),destinations=self.enviroment['notification_destination'].split(','))
            if(variables.define_monitors_variables):
                self.define_variables()
                variables.define_monitors_variables = False
            sleep(float(self.enviroment['thread_sleep_time']))
            
    def define_variables(self):
        self.enviroment = {
            'time_notification_limit': '',
            'notification_destination': '',
            'cpu_overload_counter_limit': '',
            'cpu_percent_limit': '',
            'cpu_overload_message': '',
            'memory_overload_counter_limit': '',
            'memory_percent_limit': '',
            'memory_overload_message': '',
            'disk_overload_counter_limit': '',
            'disk_percent_limit': '',
            'monitored_disk_location': '',
            'disk_overload_message': '',
            'thread_sleep_time': ''
        }
        for variable in self.enviroment:
            self.enviroment[variable] = database_actions.find_config_values(variable)
        