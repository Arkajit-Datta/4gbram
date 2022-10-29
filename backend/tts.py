import requests

url = "https://voicerss-text-to-speech.p.rapidapi.com/"

querystring = {"key":"33cc66238d854dcaac37285325dcc35c","src":"Hello, world!","hl":"en-us","r":"0","c":"mp3","f":"8khz_8bit_mono"}

headers = {
	"X-RapidAPI-Key": "891f6e26ddmsh44f4648dfe798dbp1a9a47jsna8ca77a306d3",
	"X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

with open('commentry.mp3','wb') as f:
    f.write(response.content)