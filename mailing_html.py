import smtplib, json

from json2html import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sql_query import get_schedule_recommendations

sender = "please-do-not-reply@ufl.edu"
recipient = "swehmeyer@ufl.edu"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = sender
msg['To'] = recipient

bulk = json.loads(get_schedule_recommendations())

text = "Howdy"
html = """<html><table border="0">\n"""
for key in bulk[0]:
	html += "<td>{}</td>".format(key)
#https://i.dmd.dev/idmd_app/people/select/3 ## Format for the ID href
for record in bulk:
	html += "<tr>"
	for item in record:
		if (item == 'person_id'):
			html += '\n<td><a href="https://i.dmd.dev/idmd_app/people/select/{sub}">{sub}</a></td>'.format(sub=record[item])
		else:
			html+= "<td>{}</td>""".format(record[item])
	html += "</tr>"
html += "\n</table></html>"

#print (html)##TEST

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

s = smtplib.SMTP('smtp.ufl.edu', 25)
s.sendmail(sender, recipient, msg.as_string())
s.quit()