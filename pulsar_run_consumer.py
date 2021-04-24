from pulsar_producer import PulsarProducer
from pulsar_consumer import PulsarConsumer

import threading
import time

rec_address = 'localhost'
rec_port = 6650

consumer = PulsarConsumer(rec_address, rec_port)

c_thread = threading.Thread(consumer.Run)
c_thread.start()

while True:
  time.sleep(1)
