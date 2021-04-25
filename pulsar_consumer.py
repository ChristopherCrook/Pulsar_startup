import pulsar
import time
import random

class PulsarConsumer:

  def __init__(self, address, port, input_file):
    self.config = 'pulsar://' + address
    self.config = self.config.rstrip() + ':'
    self.config = self.config.rstrip() + str(port)
    self.config = self.config.rstrip()

    random.seed(a=None, version=2)
    self.id = str(random.randint(1000, 9999))

    self.filename = self.id.rstrip() + "_"
    self.filename = self.filename.rstrip() + input_file
    self.filename = self.filename.rstrip() + "_"
    self.filename = self.filename.rstrip() + "consumer_out.txt"
    self.write = open(self.filename, "w")
    
  def Setup(self):
    self.client = pulsar.Client(self.config)
    #persistent://sample/standalone/ns1/
    self.consumer = self.client.subscribe('my-topic', self.id)

  def Run(self):
    while True:
      msg = self.consumer.receive()
      print(msg)
      self.consumer.acknowledge(msg)
      ts = time.time()
      print(ts)
      self.write.write(str(ts) + "\n")

    self.client.close()
