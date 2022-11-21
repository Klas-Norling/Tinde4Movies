#Fetches movie/serie titles, descriptions and ratings

import requests

url = "https://streaming-availability.p.rapidapi.com/search/basic"

querystring = {"country":"us","service":"netflix","type":"movie","genre":"18","page":"1","output_language":"en","language":"en"}

headers = {
	"X-RapidAPI-Key": "99ca084e1dmsh190e97f0bf7c188p10b492jsnd003864349e4",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)



