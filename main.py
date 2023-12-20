import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
#200 means api worked
#below function checks for api errors
response.raise_for_status()
#gets api data, and accesses nested values
#and assigns them to a new tuple
data = response.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
iss_position = (longitude, latitude)
print(iss_position)



