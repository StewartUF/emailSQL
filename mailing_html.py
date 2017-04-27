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

text = "Howdy"
#html = """\
"""<html>
	<head></head>
	<body>
		<table>
			<tr>
				<th>person_id</th>
				<th>site_name</th>
				<th>visit_type</th>
				<th>eta</th>
				<th>start_of_next_visit_window</th>
				<th>end_of_next_visit_window</th>
			</tr>
			<tr>
				<td>168</td>
				<td>UF</td>
				<td>Annual</td>
				<td>0-3 Months</td>
				<td>2017-04-09</td>
				<td>2017-05-07</td>
			</tr>
		</table>
	</body>
</html>
"""

bulk = json.loads(get_schedule_recommendations())
html = json2html.convert(json = bulk)

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

s = smtplib.SMTP('smtp.ufl.edu', 25)
s.sendmail(sender, recipient, msg.as_string())
s.quit()