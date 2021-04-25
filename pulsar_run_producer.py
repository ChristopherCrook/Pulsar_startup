from pulsar_producer import PulsarProducer
from pulsar_consumer import PulsarConsumer

import threading
import time
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-f", "--file", type=str, required=True, help="Input File")

args = vars(ap.parse_args())

input_file = args['file']

send_address = 'localhost'
send_port = 6650

producer = PulsarProducer(send_address, send_port, input_file)

p_thread = threading.Thread(target=producer.Setup)
p_thread.start()

producer.Run()

while True:
  time.sleep(1)
