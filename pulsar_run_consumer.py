from pulsar_producer import PulsarProducer
from pulsar_consumer import PulsarConsumer

import threading
import time
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-f", "--file", type=str, required=True, help="Input File")

args = vars(ap.parse_args())

input_file = args['file']

rec_address = 'localhost'
rec_port = 6650

consumer = PulsarConsumer(rec_address, rec_port, input_file)

c_thread = threading.Thread(target=consumer.Setup)
c_thread.start()

consumer.Run()

while True:
  time.sleep(1)
