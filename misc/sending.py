import logging
import pika
from misc.database_actions import database_actions

class notification:
    def __init__(self, message, destinations) :
        shipping_methods = {
           'logging': self.logging,
           'rabbit': self.rabbit
        }
        self.define_varaibles()
        self.message = message
        for destination in destinations:
            shipping_methods[destination]()

    def logging(self):
        logging.warning(self.message)
        
    def rabbit(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.enviroment['rabbit_host']))
        channel = connection.channel()
        channel.queue_declare(queue=self.enviroment['rabbit_queue'])
        
        channel.basic_publish(exchange='',
                      routing_key=self.enviroment['rabbit_queue'],
                      body=self.message)
        
    def define_varaibles(self):
        self.enviroment = {
            'rabbit_host': '',
            'rabbit_queue': ''
        }
        for variable in self.enviroment:
            self.enviroment[variable] = database_actions.find_config_values(variable)
