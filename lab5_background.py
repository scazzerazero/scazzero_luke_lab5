import json 
import time
import RPi.GPIO as GPIO 
GPIO.setwarnings(False) 

from stepper_class import Stepper

StepperObject=Stepper([18,21,22,23],16)# controller inputs: in1, in2, in3, in4. Led pin=16

while True:
  try:
    with open("lab5_text.txt",'r') as f:
      form=json.load(f)
      time.sleep(0.5)
      print(form)
    if form['angleVal'] != None:
      angle=int(form['angleVal'])
      StepperObject.goAngle(angle)

      
    if str(form['zerobutton'])=="ZeroMotor":
      print("ZERO DAT BITCH PLEASE")
      StepperObject.Zero()
      time.sleep(3)
      with open('lab5_text.txt','w') as f:
	      json.dump({'angleVal':0,'zerobutton':None},f)
      #print("wrote this to txt file= "+str({'angleVal':form['angleVal'],'zerobutton':None}))
  except KeyboardInterrupt:
    print("\nExiting!")
    GPIO.cleanup()
    break

#now convert this into a class. So you can make stepper object and make some methods to make it do the thing you want.
#two methods. Move to an angle. Convert half steps to angle. we calcualted that conversion in the notes. another instance variable must be the current angle too.
