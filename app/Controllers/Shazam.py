import requests

async def getFields(artist, title):
 url = "https://shazam.p.rapidapi.com/search"

 querystring = {"term":title,"locale":"en-US","offset":"0","limit":"1"}

 headers = {
	"X-RapidAPI-Key": "3f4bfea3edmshb24e5a367ae4d97p1a3366jsn30c957ba2712",
	"X-RapidAPI-Host": "shazam.p.rapidapi.com"
 }

 response = requests.get(url, headers=headers, params=querystring)

 print(response.json())