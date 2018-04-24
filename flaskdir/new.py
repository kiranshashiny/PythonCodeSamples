import requests
import requests.exceptions

try:
	payload = {'quote':'INFY'}
	r = requests.get( 'https://finance.yahoo.com/', params=payload )

except requests.exceptions.RequestException :

	print ("could not connect to the remote location. " )
else:
	print (r.url)
	print (r.status_code)
	#print (r.headers)
	print ("Content  Type = ", r.headers.get('content-type'))
	print (r.request.headers)

