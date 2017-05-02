import smtplib, json

from json2html import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sql_query import get_schedule_recommendations

"""This script emails a sparsley formatted HTML table of data for 
scheduling iDMD patients' next visits. 

The table includes links to each patients' records via their 
person_id. This script executes sql_query when run. -SDW 5/2/17"""

# Set message parameters
sender = "please-do-not-reply@ufl.edu"
recipient = "swehmeyer@ufl.edu"
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = sender
msg['To'] = recipient

# Get JSON format content from sql_query
bulk = json.loads(get_schedule_recommendations())

# Set person_id link prepath to managable variable name
person = "https://i.dmd.dev/idmd_app/people/select/"

# Create message content
text = "Howdy"
html = """<html><table border="0">\n"""
for key in bulk[0]:
	html += "<td>{}</td>".format(key)
for record in bulk:
	html += "<tr>"
	for item in record:
		if (item == 'person_id'):
			html += '\n<td><a href="{one}{sub}">{sub}</a></td>'.format(one=person, sub=record[item])
		else:
			html+= "<td>{}</td>""".format(record[item])
	html += "</tr>"
html += "\n</table></html>"

# Assign message content
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
msg.attach(part1)
msg.attach(part2)

# Send the message and quit the service
s = smtplib.SMTP('smtp.ufl.edu', 25)
s.sendmail(sender, recipient, msg.as_string())
s.quit()