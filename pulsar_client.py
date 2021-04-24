from pulsar_producer import PulsarProducer
from pulsar_consumer import PulsarConsumer

import threading
import time

send_address = 'localhost'
send_port = 6650

rec_address = 'localhost'
rec_port = 6650

consumer = PulsarConsumer(rec_address, rec_port)
producer = PulsarProducer(send_address, send_port)

c_thread = threading.Thread(consumer.Run)
c_thread.start()

p_thread = threading.Thread(producer.Run)
p_thread.start()

while True:
  time.sleep(1)
