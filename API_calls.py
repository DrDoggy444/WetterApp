from requests import *
#Konstanten
BASE_URL = 'http://api.weatherapi.com/v1'
API_KEY = '6668ee1162af454fa6f65814231512'

class HTTPRequests(Request):
    def __init__(self, method=None, 
                 url=BASE_URL, headers={'key' : API_KEY}, 
                 files=None, data=None, params=None, 
                 auth=None, cookies=None, hooks=None, 
                 json=None) -> None:
        super().__init__(method, url, headers, files, data, params, auth, cookies, hooks, json)
        self.headers = headers
        self.url    = url

    def CheckOnlineStatus(self)-> bool:
        response = request('GET',self.url + '/current.json', headers = self.headers, params={'q' : 'Paris'})
        return (response.status_code == 200)
    
    def getCurrentWeather(self, city):
        response = request('GET',self.url + '/current.json', headers = self.headers, params={'q' : city})
        tmp = response.text
        i = tmp.find('temp_c') + 8 #substring finden
        temperature = tmp[i:i+4]+'°C'
        return temperature

test = HTTPRequests()
print(test.CheckOnlineStatus())
print(test.getCurrentWeather('Paderborn'))