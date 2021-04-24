from pulsar_producer import PulsarProducer
from pulsar_consumer import PulsarConsumer

import threading
import time

rec_address = '129.114.25.176'
rec_port = 6550

consumer = PulsarConsumer(rec_address, rec_port)

c_thread = threading.Thread(target=consumer.Setup)
c_thread.start()

time.sleep(15)

consumer.Run()

while True:
  time.sleep(1)
