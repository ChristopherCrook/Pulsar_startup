import pulsar
import time

class PulsarProducer:

  def __init__(self, address, port):
    self.config = 'pulsar://' + address
    self.config = self.config.rstrip() + ':'
    self.config = self.config.rstrip() + str(port)
    self.config = self.config.rstrip()

    self.filename = "producer_out.txt"
    self.write = open(self.filename, "w")
    
  def Setup(self):
    self.client = pulsar.Client(self.config)
    time.sleep(10)
    #persistent://sample/standalone/ns1/
    self.producer = self.client.create_producer('my-topic')

  def Run(self):
    self.count = 0
    self.kill_switch = False
    while self.kill_switch == False:
      if self.kill_switch == False:
        self.Send_Tiny()
      if self.kill_switch == False:
        self.Send_Small()
      if self.kill_switch == False:
        self.Send_Medium()
      if self.kill_switch == False:
        self.Send_Large()
      if self.kill_switch == False:
        self.Send_XLarge()

    self.client.close()
    
  def Send_Tiny(self):
    file1 = open('tiny.txt', 'r')
    count = 0
  
    while True:
      if self.count >= 1000:
        self.kill_switch = True
        break
      count += 1
    
      line = file1.readline()
    
      if not line:
        break
      ts = time.time()
      print(ts)
      self.write.write(str(ts) + "\n")
      self.producer.send(line.encode('utf-8'))
      self.count = self.count + 1
      
    file1.close()
  
  def Send_Small(self):
    file1 = open('small.txt', 'r')
    count = 0
  
    while True:
      if self.count >= 1000:
        self.kill_switch = True
        break
      count += 1
    
      line = file1.readline()
    
      if not line:
        break
      ts = time.time()
      print(ts)
      self.write.write(str(ts) + "\n")
      self.count = self.count + 1
      self.producer.send(line.encode('utf-8'))
      self.count = self.count + 1
      
    file1.close()
  
  def Send_Medium(self):
    file1 = open('medium.txt', 'r')
    count = 0
  
    while True:
      if self.count >= 1000:
        self.kill_switch = True
        break
      count += 1
    
      line = file1.readline()
    
      if not line:
        break
      ts = time.time()
      print(ts)
      self.write.write(str(ts) + "\n")
      self.producer.send(line.encode('utf-8'))
      self.count = self.count + 1
      
    file1.close()
  
  def Send_Large(self):
    file1 = open('large.txt', 'r')
    count = 0
  
    while True:
      if self.count >= 1000:
        self.kill_switch = True
        break
      count += 1
    
      line = file1.readline()
    
      if not line:
        break
      ts = time.time()
      print(ts)
      self.write.write(str(ts) + "\n")
      self.producer.send(line.encode('utf-8'))
      self.count = self.count + 1
      
    file1.close()
  
  def Send_XLarge(self):
    file1 = open('xlarge.txt', 'r')
    count = 0
  
    while True:
      if self.count >= 1000:
        self.kill_switch = True
        break
      count += 1
    
      line = file1.readline()
    
      if not line:
        break
      ts = time.time()
      print(ts)
      self.write.write(str(ts) + "\n")
      self.producer.send(line.encode('utf-8'))
      self.count = self.count + 1
      
    file1.close()
  
