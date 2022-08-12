import os
from .database_actions import database_actions
from misc.animations import animations

class shell():
    def __init__(self):
        while 1:
            command = input('config: ')
            if(command == 'clear'):
                os.system(command)
                animations.start()
            elif(command == 'show'):
                for config in database_actions.find_all_configs():
                    print(config)
            elif(command == 'update'):
                name = input('name: ')
                value = input('value: ')
                accept = input(f"O resultado sera ('{name}', '{value}') tem certeza disso? s/n: ")
                if(accept.capitalize() == 'S'):
                    print(database_actions.update_config(name,value))
            else:
                print('Comando invalido')