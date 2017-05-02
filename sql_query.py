import pymysql, datetime, json, pdb

"""
The script iterates through recommended_visits_with_scheduling_report_details 
and creates a JSON string containing patient scheduling data.

The JSON is a list of each row with the corresponding data in dictionaries;
person_id, site_name, visit_type, etc.-SDW 5/2/17
"""

def get_schedule_recommendations():

	# Connect to database and access rows and columns.
	connection = pymysql.connect(host = 'i.dmd.dev', user = 'admin', 
		password = 'password', db = 'app_database')
	with connection.cursor() as cursor:
		sql = "SELECT * FROM recommended_visits_with_scheduling_report_details"
		cursor.execute(sql)
		rows = [x for x in cursor]
		cols = [x[0] for x in cursor.description]
		boys = []

		# Build list of dictionaries.
		for row in rows:
			boy = {}
			for prop, val in zip(cols, row):
				if (isinstance(val, datetime.date)):
					val = str(val)
				boy[prop] = val
			boys.append(boy)

		# Convert list of dictionaries to JSON.
		boysJSON = json.dumps(boys)
		return boysJSON
		connection.close()

if __name__ == '__main__':
	get_schedule_recommendations()