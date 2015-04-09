from googleplaces import GooglePlaces, types, lang
import re,MySQLdb
import shutil
import requests

db = MySQLdb.connect(unix_socket='.../mysql.sock', host="127.0.0.1", # your host, usually localhost
                     user="root", # your username
                      passwd="root", # your password
                      db="collegeList")

def store(place):
		global i
		global db
		cursor = db.cursor() 
		flag=True
		query = "INSERT INTO place_name (id, name, latitude, longitude) VALUES ('%d', '%s' , '%s','%s');" % ( i,  place.name,place.geo_location['lat'],place.geo_location['lng'])
		try :
			cursor.execute(query)
		except :
			flag=False
			i=i-1
			pass
			
		db.commit()
		print "stored"


google_places = GooglePlaces('#yourgooleplaceskey#')

i = 124

def show_results(lat,lng):
	global i
	query_result = google_places.text_search(lat_lng={'lat': lat , 'lng': lng}, radius=2000, types=['university'])
	for place in query_result.places:
   		 print place.name
		 store(place)
		 print i
		 i=i+1;

f=open('place-list.txt', 'r')
for line in f:
        data=re.split(',|:| |\n',line)
        show_results(data[3],data[5])


