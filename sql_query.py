#Stewart Wehmeyer
#4/19/17
import pymysql, datetime, json, pdb

"""
1. Get appropriate SQL query (select * from 
	recommended_visits_with_scheduling_report_details) passed to python
2. Put the query (result) into HTML table so it is legible
3. Email query
"""

def get_schedule_recommendations():
	connection = pymysql.connect(host = 'i.dmd.dev', user = 'admin', 
		password = 'password', db = 'app_database')
	with connection.cursor() as cursor:
		sql = "SELECT * FROM recommended_visits_with_scheduling_report_details"
		cursor.execute(sql)
		#result = cursor.fetchall()
		#temporarily limit return to first 5 rows ... for ease of testing
		#result = cursor.fetchmany(size = 5)
		rows = [x for x in cursor]
		cols = [x[0] for x in cursor.description]
		boys = []
		for row in rows:
			#print (type(row), row)##SUCCESS
			boy = {}
			for prop, val in zip(cols, row):
				if (isinstance(val, datetime.date)):
					val = str(val)
				#print (type(val))##TEST
				boy[prop] = val
			boys.append(boy)
			"""if (boy["person_id"] == 61):
				pdb.set_trace()"""##TEST
		boysJSON = json.dumps(boys)
		#print(boysJSON)##TEST
		return boysJSON
		connection.close()

if __name__ == '__main__':
	get_schedule_recommendations()