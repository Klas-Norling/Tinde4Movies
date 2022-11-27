#Fetches movie/serie titles, descriptions, ratings

import requests
import json

#Create the gui and such with kivy, look youtube video to know how to work with it


#Retrives the data from netflix in json format and calls the parseData function that sorts and parses the json data
def getData():
    url = "https://streaming-availability.p.rapidapi.com/search/basic"

    querystring = {"country":"us","service":"netflix","type":"movie","genre":"18","page":"1","output_language":"en","language":"en"}

    headers = {
        "X-RapidAPI-Key": "99ca084e1dmsh190e97f0bf7c188p10b492jsnd003864349e4",
        "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    titles, descriptions, years = parseData(response.text)
    return titles, descriptions, years
    


#Parses data from json response by making it into a python dict and looping through keys 'title', 'overview', 'year' for now
def parseData(json_data):
    titles = []
    descriptions = []
    years = []

    jsonToDict = json.loads(json_data)

    for i in range(len(jsonToDict['results'])):
        titles.append(jsonToDict['results'][i]['title'])
        descriptions.append(jsonToDict['results'][i]['overview'])
        years.append(jsonToDict['results'][i]['year'])

    return titles, descriptions, years





getData()





