import pulsar
import time

class PulsarProducer:

  def __init__(self, address, port):
    config = 'pulsar://' + address
    config = config.rstrip() + str(port)
    config = config.rstript()
    self.client = pulsar.Client(config)
    self.producer = self.client.create_producer('my-topic')

  def Run(self):
    for i in range(1000):
      self.Send_Tiny()
      self.Send_Small()
      self.Send_Medium()
      self.Send_Large()
      self.Send_XLarge()

    self.client.close()
    
  def Send_Tiny(self):
  file1 = open('tiny.txt', 'r')
  count = 0
  
  while True:
    count += 1
    
    line = file1.readline()
    
    if not line:
      break
    ts = time.time()
    print(ts)
    self.producer.send(line.encode('utf-8'))
  
  def Send_Small(self):
    file1 = open('small.txt', 'r')
    count = 0
  
    while True:
      count += 1
    
      line = file1.readline()
    
      if not line:
        break
      ts = time.time()
      print(ts)
      self.producer.send(line.encode('utf-8'))
      
    file1.close()
  
  def Send_Medium(self):
    file1 = open('medium.txt', 'r')
    count = 0
  
    while True:
      count += 1
    
      line = file1.readline()
    
      if not line:
        break
      ts = time.time()
      print(ts)
      self.producer.send(line.encode('utf-8'))
      
    file1.close()
  
  def Send_Large(self):
    file1 = open('large.txt', 'r')
    count = 0
  
    while True:
      count += 1
    
      line = file1.readline()
    
      if not line:
        break
      ts = time.time()
      print(ts)
      self.producer.send(line.encode('utf-8'))
      
    file1.close()
  
  def Send_XLarge(self):
    file1 = open('xlarge.txt', 'r')
    count = 0
  
    while True:
      count += 1
    
      line = file1.readline()
    
      if not line:
        break
      ts = time.time()
      print(ts)
      self.producer.send(line.encode('utf-8'))
      
    file1.close()
  
