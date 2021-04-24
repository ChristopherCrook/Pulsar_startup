import pulsar
import time

class PulsarConsumer:

  def __init__(self, address, port):
    config = 'pulsar://' + address
    config = config.rstrip() + str(port)
    config = config.rstript()
    self.client = pulsar.Client(config)
    self.consumer = self.client.subscribe('my-topic', 'my-subscription')

  def Run(self):
    while True:
      msg = self.consumer.receive()
      print(msg.decode('utf-8'))
      self.consumer.acknowledge(msg)
      ts = time.time()
      print(ts)

    self.client.close()
