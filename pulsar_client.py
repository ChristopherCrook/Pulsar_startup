from pulsar_producer import PulsarProducer
from pulsar_consumer import PulsarConsumer

import threading
import time

consumer = PulsarConsumer()
producer = PulsarProducer()

c_thread = threading.Thread(consumer.Run)
c_thread.start()

p_thread = threading.Thread(producer.Run)
p_thread.start()

while True:
  time.sleep(1)
