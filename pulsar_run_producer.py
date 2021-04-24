from pulsar_producer import PulsarProducer
from pulsar_consumer import PulsarConsumer

import threading
import time

send_address = 'localhost'
send_port = 6650

producer = PulsarProducer(send_address, send_port)

p_thread = threading.Thread(target=producer.Setup)
p_thread.start()

time.sleep(15)
producer.Run()

while True:
  time.sleep(1)
