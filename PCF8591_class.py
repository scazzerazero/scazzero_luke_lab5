#To check address: sudo i2cdetect -y 1

import smbus

class PCF8591:

  def __init__(self,address): #the "self" has attritubtes. Here it only has one, an address.
    #self.___ represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class in python. It binds the attributes with the given arguments. The reason you need to use self is because Python does not use the @ syntax to refer to instance attributes.
    self.bus = smbus.SMBus(1) #newer Pis use bus no.1
    self.address = address #the I2C device lives at a address in the bus
  #the "self" can do things! Here we're creating our read() and write() methods for it to use:
  def read(self,chn): #channel
      try:
          # Read/write 1 byte from/to a specific register of a given device address
          self.bus.write_byte(self.address, 0x40 | chn)  # 01000000
          self.bus.read_byte(self.address) # dummy read to start conversion
          #note about the 8 control bits for ADC:
            #0,analog out enabled?,analog in channel select,analog in channel select,0,A/D channel number 0 1 2 or 3
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)

  def write(self,val):
      try:
          self.bus.write_byte_data(self.address, 0x40, int(val))
      except Exception as e:
          print ("Error: Device address: 0x%2X \n%s" % (self.address,e))
