from pulsar_producer import PulsarProducer
from pulsar_consumer import PulsarConsumer

import threading
import time
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-f", "--file", type=str, required=True, help="Input File")
ap.add_argument("-p", "--producers", type=int, required=True, help="Producer instances")
ap.add_argument("-c", "--consumers", type=int, required=True, help="Consumer instances")

args = vars(ap.parse_args())

input_file = args['file']
producers = args['producers']
consumers = args['consumers']

send_address = 'localhost'
send_port = 6650

rec_address = 'localhost'
rec_port = 6650

producer_array = []
consumer_array = []

if producers < 2:
  producer = PulsarProducer(send_address, send_port, input_file)
  producer.Setup()
  producer_array.append(producer)
else:
  for i in range(producers):
    temp = PulsarProducer(send_address, send_port, input_file)
    temp.Setup()
    producer_array.append(temp)

if consumers < 2:
  consumer = PulsarConsumer(rec_address, rec_port, input_file)
  consumer.Setup()
  consumer_array.append(consumer)
else:
  for i in range(consumers):
    temp = PulsarConsumer(send_address, send_port, input_file)
    temp.Setup()
    consumer_array.append(temp)
    
for i in consumer_array:
  p_thread = threading.Thread(target=i.Run)
  p_thread.start()
  
for i in producer_array:
  p_thread = threading.Thread(target=i.Run)
  p_thread.start()
  

while True:
  time.sleep(1)
