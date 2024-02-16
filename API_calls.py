from requests import *



class HTTPRequests(Request):
    """Dieses Modul ist um Abfragen von Wetterdaten von api.weatherapi.com gedacht\n 
    Mit der Variable 'WeatherAPI' können dessen Funktionen genutzt werden.
         
    Zur Verfügung stehende Funktionen:
    :CheckOnlineStatus() --> Ist der Service verfügbar?
    :getCurrentWeather(city) --> gibt die aktuelle °C für die angegebene Stadt zurück"""
    #Attribute
    BASE_URL = 'http://api.weatherapi.com/v1'
    API_KEY = '6668ee1162af454fa6f65814231512'

    def __init__(self, method=None, 
                 url=BASE_URL, headers={'key' : API_KEY}, ) -> None:
        super().__init__(method, url, headers)
        self.headers = headers
        self.url    = url

    def CheckOnlineStatus(self)-> bool:
        try:
            response = request('GET',self.url + '/current.json', headers = self.headers, params={'q' : 'Paris'})
        except:
            return False
        return (response.status_code == 200)
    
    def __getData(self,city):
        """Hauptabfrage
        :city = Stadt von der die Wetterdaten abgefragt werden sollen"""
        response = request('GET',self.url + '/current.json', headers = self.headers, params={'q' : city})
        tmp = response.text
        return tmp
    
    def getCurrentWeather(self, city):
        city = self.__getData(city)
        i = tmp.find('temp_c') + 8 # "find" nimmt nur den ersten Index als Ergebniss --> i + 8 um Wert zu finden
        tmp = tmp[i:i+4].replace(',','') + '°C' # xx.x°C, das Replace ist im Falle von einstelliger Gradzahl benötigt
        temperature = tmp
        return temperature
    

    def validRequest(self,response):
        if response != '":{"°C':
            return True
        else:
            return False


WeatherAPI = HTTPRequests()
