import json,requests,re,MySQLdb

i=0

db = MySQLdb.connect(unix_socket='#pathtoyoursocket#', host="127.0.0.1", # your host, usually localhost
                     user="root", # your username
                      passwd="root", # your password
                      db="collegeList")

def store(data):
	global i 
	print data
	print '*****************',i,'**************'
	i=i+1
	
def show_results(lat,lng,npt):
	url = 'https://maps.googleapis.com/maps/api/place/search/json'
	if npt is not None:
		params = dict(location=lat+','+lng,radius='2000',sensor='false',key='#keyhere#',keyword='colleges',pagetoken=npt,types='university')
	else:
		params = dict(location=lat+','+lng,radius='2000',sensor='false',key='#keyhere#',keyword='colleges', types='university')

	headers=dict(scheme="https",version="HTTP/1.1",accept="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",accept-encoding="gzip,deflate,sdch", accept-language="en-US,en;q=0.8",cache-control="max-age=0",user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.72 Safari/537.36")	
	resp = requests.get(url=url, params=params, headers=headers)
        print resp.url
	data = json.loads(resp.content)
	store(data)
	if 'next_page_token' in data:
		show_results(lat,lng,data['next_page_token'])


f=open('list.txt', 'r')
for line in f:
	data=re.split(',|:| |\n',line)
	show_results(data[3],data[5],None)
