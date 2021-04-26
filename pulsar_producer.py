import pulsar
import time
import random

class PulsarProducer:

  def __init__(self, address, port, input_file):
    self.file = input_file
    self.file = self.file.rstrip() + '.txt'
    self.file = self.file.rstrip()
    
    self.config = 'pulsar://' + address
    self.config = self.config.rstrip() + ':'
    self.config = self.config.rstrip() + str(port)
    self.config = self.config.rstrip()
    
    random.seed(a=None, version=2)
    self.id = str(random.randint(1000, 9999))

    self.filename = self.id.rstrip() + "_"
    self.filename = self.filename.rstrip() + input_file
    self.filename = self.filename.rstrip() + "_"
    self.filename = self.filename.rstrip() + "producer_out.csv"
    self.write = open(self.filename, "w")
    
  def Setup(self):
    self.client = pulsar.Client(self.config)
    #persistent://sample/standalone/ns1/
    self.producer = self.client.create_producer('my-topic')

  def Run(self):
    count = 0
    file1 = open(self.file, 'r')
    lastLine = None
    while count < 1000:
      line = file1.readline()
      if line:
        st = time.time()
        self.producer.send(line.encode('utf-8'))
        at = time.time()
        self.write.write(str(st) + "," + str(at) + ",\n")
        lastLine = line
      else:
        st = time.time()       
        self.producer.send(lastLine.encode('utf-8'))
        at = time.time()
        self.write.write(str(st) + "," + str(at) + "\n")
       
      count = count + 1
        
    file1.close()
    self.client.close()
    print("Count is %s" % str(count))
