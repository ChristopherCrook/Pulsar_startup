import pulsar
import time

class PulsarConsumer:

  def __init__(self):
    self.client = pulsar.Client('pulsar://localhost:6651')
    self.consumer = self.client.subscribe('my-topic', 'my-subscription')

  def Run(self):
    while True:
      msg = self.consumer.receive()
      print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
      self.consumer.acknowledge(msg)
      ts = time.time()
      print(ts)

    self.client.close()
