from requests import *
#Konstanten
BASE_URL = 'http://api.weatherapi.com/v1'
API_KEY = '6668ee1162af454fa6f65814231512'

class HTTPRequests(Request):
    def __init__(self, method=None, 
                 url=BASE_URL, headers={'key' : API_KEY}, ) -> None:
        super().__init__(method, url, headers, files, data, params, auth, cookies, hooks, json)
        self.headers = headers
        self.url    = url

    def CheckOnlineStatus(self)-> bool:
        response = request('GET',self.url + '/current.json', headers = self.headers, params={'q' : 'Paris'})
        return (response.status_code == 200)
    
    def getCurrentWeather(self, city):
        response = request('GET',self.url + '/current.json', headers = self.headers, params={'q' : city})
        tmp = response.text
        i = tmp.find('temp_c') + 8 # "find" nimmt nur den ersten Index als Ergebniss --> i + 8 um Wert zu finden
        tmp = tmp[i:i+4].replace(',','') + '°C'
        temperature = tmp
        return temperature

call = HTTPRequests()
