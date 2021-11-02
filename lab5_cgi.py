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
print("value attatched to key 1: %s <br>"% form.getvalue('anglebutton')) #feed .getvalue a 'key'
print("value attatched to key 2: %s <br>"% form.getvalue('zerobutton'))
print("The angle value sent in: %s <br>"% form.getvalue('angleVal'))


print('<html>')
print('<head><title>Stepper motor program! (CGI)</title></head>')
print('<body style="background-color:lightgreen;">')
print('<h3>What ANGLE we goin to?</h3>')
print('<form action="/cgi-bin/lab5_cgi.py" method="POST";text-align:center>')
print(' <input type="text" name="angleVal" min="0" max="360" placeholder="from 0 to 360">')

print('  <input type="submit" value="SubmitAngle">')
print('  <br><br>')
print('  <input type="submit" name ="zerobutton" value="ZeroMotor">')
print('</form>')
print('</body>')
print('</html>')