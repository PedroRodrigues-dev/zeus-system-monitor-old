import logging
import os
import sys
from threading import Thread
from config.database import sqlite
from misc.animations import animations
from misc.shell import shell
from monitors.monitor import monitor
import misc.variables as variables

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    animations.start()
    print('Carregando variaveis de ambiente')
    logging.basicConfig(filename='system.log' ,format='%(asctime)s : [%(levelname)s] : %(message)s', level=logging.DEBUG)
    print('Iniciando banco de dados')
    sqlite()
    variables.define_monitors_variables = False
    variables.monitors_loop = True
    monitors = ['CPU', 'memoria', 'disco']
    # 0 = cpu / 1 = memory / 2 = disk
    for i in range(3):
        print(f'Iniciando monitor de {monitors[i]}')
        Thread(target=monitor, args=(i,)).start()
    print('Iniciando shell')
    logging.info('Iniciado')
    try:
        Thread(target=shell()).start()
    except:
        variables.monitors_loop = False
        logging.info('Finalizado')
    
if __name__ == '__main__':
    sys.exit(main())
