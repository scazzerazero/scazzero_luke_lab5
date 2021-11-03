#!/usr/bin/python37all

#put this file in /usr/lib/cgi-bi and change permissions (sudo chmod 755 led.py)
    #for cgi code to be executable we must make it executable by anyone. Chmod changes permissions on files. Gives anyone read and execute permissions.

import json
import cgi
import cgitb #for exception handling
cgitb.enable()




print('Content-type:text/html\n\n <!-- every print line will now be interp as html-->')

form=cgi.FieldStorage()
print('<br>')
print(' The whole form:: '+str(form)+'<br>')
print('<br>')
print("value attatched to zerobutton key: %s <br>"% form.getvalue('zerobutton'))
print("The angle value sent in: %s <br>"% form.getvalue('angleVal'))
#creating dict: {angleVal:180,zerobutton:None or ZeroMotor}
formdict={'angleVal':form.getvalue('angleVal'),'zerobutton':form.getvalue('zerobutton')}
print('<br>')
print('The formdict being submitted: %s'% formdict)
#loading up json file:
with open('lab5_text.txt','w') as f:
	json.dump(formdict,f)

#begin generation of wen page showing current state:
print('<html>')
print('<head><title>Stepper motor program! (CGI)</title></head>')
print('<body style="background-color:lightgreen;">')
print('<h3>What ANGLE we goin to?</h3>')
print('<form action="/cgi-bin/lab5_cgi.py" method="POST";text-align:center>')
print(' <input type="text" name="angleVal" min="0" max="360" placeholder="from 0 to 360">')

print('  <input type="submit" value="SubmitAngle">')
print('  <br><br>')
print('  <input type="submit" name ="zerobutton" value="ZeroMotor">')


from urllib.request import urlopen #use to send/recieve data
from urllib.parse import urlencode #use to structure a GET string
#Thingspeak
api="28S5DZU2FVPFIAFJ"
params=formdict.update({"api_key":api})#append the data dictionary with api_key info
print('<br>')
print(params)

#params=urlencode(params)
#url="https://api.thingspeak.com/update?"+params


print('</form>')
print('</body>')
print('</html>')