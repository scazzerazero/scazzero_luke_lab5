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
#print(' The whole form:: '+str(form)+'<br>')
print('<br>')
#print("value attatched to zerobutton key: %s <br>"% form.getvalue('zerobutton'))
#print("The angle value sent in: %s <br>"% form.getvalue('angleVal'))
#creating dict: {angleVal:180,zerobutton:None or ZeroMotor}
formdict={'angleVal':form.getvalue('angleVal'),'zerobutton':form.getvalue('zerobutton')}
print('<br>')
#print('The formdict being submitted: %s'% formdict)
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
params=formdict #use data we were storing in formdict and sending to txt file
api="28S5DZU2FVPFIAFJ"

print('<br>')
print('<br>')
if formdict.get('angleVal') != None:
  anglevalue=formdict.get('angleVal')
elif formdict.get('angleVal')==None:
  anglevalue='0'
  
url="https://api.thingspeak.com/update?api_key="+api+"&"+str(1)+"="+ anglevalue
#response=urlopen(url)
#print(response.status,response.reason)

#the two plots:
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1557902/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Angle+vs.+Time&type=line"></iframe>')

print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1557902/widgets/375671"></iframe>')



print('</form>')
print('</body>')
print('</html>')