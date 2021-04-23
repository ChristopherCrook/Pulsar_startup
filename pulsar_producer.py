import pulsar
import time

class PulsarProducer:

  def __init__(self):
    self.client = pulsar.Client('pulsar://localhost:6443')
    self.producer = self.client.create_producer('my-topic')

  def Run(self):
    for i in range(25):
      self.producer.send(('Hello-%d' % i).encode('utf-8'))
      ts = time.time()
      print(ts)
      time.sleep(1)

    self.client.close()
