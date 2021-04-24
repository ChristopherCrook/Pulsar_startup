from pulsar_producer import PulsarProducer
from pulsar_consumer import PulsarConsumer

import threading
import time

send_address = 'localhost'
send_port = 5556

producer = PulsarProducer(send_address, send_port)

p_thread = threading.Thread(producer.Run)
p_thread.start()

while True:
  time.sleep(1)
