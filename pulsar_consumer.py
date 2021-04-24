import pulsar
import time

class PulsarConsumer:

  def __init__(self, address, port):
    config = 'pulsar://' + address
    config = config.rstrip() + str(port)
    config = config.rstrip()
    self.client = pulsar.Client(config)
    self.consumer = self.client.subscribe('my-topic', 'my-subscription')
    self.filename = "consumer_out.txt"
    self.write = open(self.filename, "w")

  def Run(self):
    while True:
      msg = self.consumer.receive()
      print(msg.decode('utf-8'))
      self.consumer.acknowledge(msg)
      ts = time.time()
      print(ts)
      self.write.write(ts + "\n")

    self.client.close()
