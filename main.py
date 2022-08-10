import logging
import os
import sys
from threading import Thread
from config.database import sqlite
from monitors.monitor import monitor
from dotenv import load_dotenv

def main():
    load_dotenv()
    logging.basicConfig(format='%(asctime)s : [%(levelname)s] : %(message)s', handlers=[
    logging.FileHandler(os.environ.get('log_file_name')),
    logging.StreamHandler(sys.stdout)
    ])
    sqlite()

    # 0 = cpu / 1 = memory / 2 = disk
    for i in range(3):
        Thread(target=monitor, args=(i,)).start()
    
if __name__ == '__main__':
    sys.exit(main())
