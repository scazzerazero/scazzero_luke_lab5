import RPi.GPIO as GPIO 
import time 
#import PCF8591 #from a directory



class Stepper:

  def __init__(self,pins):  #constructor
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
      GPIO.setup(pin, GPIO.OUT, initial=0)
    self.sequence= [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
    [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ] #sequence of steps to go through on whole cycle
    self.pins=pins
    self.angle=0 #initial angle
    self.state=0 #current position in stator sequence
    #self.ADC=PCF8591(0x48) # By composition, we're extending the PCF8591 class. using it to define our Joystick class's attribute self.ADC

    
  def goAngle(self,targetAngle):
    #diff will give you the angle you should move to get to target angle
    diff = ( targetAngle - self.angle + 180 ) % 360 - 180;
    if (diff )< -180:
      diff += 360 
    stepsReq=diff*(512*8)/(360) #512*8 is 1 rev in the ccw direction.
    sign = lambda x: (1, -1)[x<0]
    self.__moveSteps(int(abs(stepsReq)),sign(diff)) #steps required, direction (+/- 1)
    self.angle=targetAngle #the current angle is now the angle we just moved to!
    
  #def Zero(self):
  #  self.ADC.read(0) #channel zero
  
  #in class motor control
  
  def __delay_us(self,tus): # use microseconds to improve time resolution
    endTime = time.time() + float(tus)/ float(1E6)
    while time.time() < endTime:
      pass
  def __halfstep(self,dir):
    #dir=+/- 1 (ccw/cw)
     
    self.state+=dir#increment forward, decrement reverse
    #we dont want to go past the list. if we rolloff reset ourselves at beginning open. was previously state +=1
    #print("state= "+str(state))
    if self.state>7: self.state=0 # we really ony need to check 8 or -1
    elif self.state<0:self.state=7
    for pin in range(4):
      #print("GPIO output: sequence["+str(state)+"]"+"["+str(pin)+"]"+"= "+ str(sequence[state][pin]))
      GPIO.output(self.pins[pin], self.sequence[self.state][pin]) #indexes sequence [chunk] then the pins in it
    self.__delay_us(1000)


    #make another private method called...move a certain # half st
  def __moveSteps(self,steps,dir):
    #move actuation sequence a given number of half steps
    for step in range(steps):
      #print("iterating step in range(steps): "+str(step))
      self.__halfstep(dir) #call halfsteps that number of times in right direction. Thats it.and


