import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

# Define the pin sequence for counter-clockwise motion, noting that
# two adjacent phases must be actuated together before stepping to
# a new phase so that the rotor is pulled in the right direction:
sequence= [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
        [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ] #sequence of steps to go through on whole cycle
#512 of these sequences will rotate me 360/8 deg

state = 0 #current position in stator sequence

def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:

    pass

def halfstep(dir):
  #dir=+/- 1 (ccw/cw)
  global state
  state+=dir#increment forward, decrement reverse
  #we dont want to go past the list. if we rolloff reset ourselves at beginning open. was previously state +=1
  print("state= "+str(state))
  if state>7: state=0 # we really ony need to check 8 or -1
  elif state<0:state=7
  for pin in range(4):
    print("GPIO output: sequence["+str(state)+"]"+"["+str(pin)+"]"+"= "+ str(sequence[state][pin]))
    GPIO.output(pins[pin], sequence[state][pin]) #indexes sequence [chunk] then the pins in it

  delay_us(1000)
 


#make another private method called...move a certain # half st
def moveSteps(steps,dir):
  #move actuation sequence a given number of half steps
  for step in range(steps):
    print("iterating step in range(steps): "+str(step))
    halfstep(dir) #call halfsteps that number of times in right direction. Thats it.and


try:

  moveSteps(512*8,1) #512*8 is 1 step in the ccw direction.

except:
  pass
GPIO.cleanup() 

#now convert this into a class. So you can make stepper object and make some methods to make it do the thing you want.
#two methods. Move to an angle. Convert half steps to angle. we calcualted that conversion in the notes. another instance variable must be the current angle too.
