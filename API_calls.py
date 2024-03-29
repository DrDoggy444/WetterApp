from requests import *
class HTTPRequests(Request):
    """Dieses Modul ist um Abfragen von Wetterdaten von api.weatherapi.com gedacht\n 
    Mit der Variable 'WeatherAPI' können dessen Funktionen genutzt werden.
         
    Zur Verfügung stehende Funktionen:
    :CheckOnlineStatus() --> Ist der Service verfügbar?
    :getCurrentWeather(city) --> gibt die aktuelle °C für die angegebene Stadt zurück
    :validRequest() --> prüft die Abfrage,ob die Stadt in der Datenbank existiert"""
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
            response = request('GET',self.url + '/current.json', headers = self.headers, params={'q' : 'Paris'},timeout=20)
        except:
            return False
        return (response.status_code == 200)
    
    def __getData(self,city):
        """Hauptabfrage, wird von allen weiteren Funktionen verwendet
        :city = Stadt von der die Wetterdaten abgefragt werden sollen"""
        response = request('GET',self.url + '/current.json', headers = self.headers, params={'q' : city})
        tmp = response.text
        return tmp
    
    def getTemperatur(self, tmp):
        tmp = self.__getData(tmp)
        i = tmp.find('temp_c') + 8 # "find" nimmt nur den ersten Index als Ergebniss --> i + 8 um richtigen Wert zu finden
        tmp = tmp[i:i+4].replace(',','') + '°C' # xx.x°C, das Replace ist im Falle von einstelliger Gradzahl benötigt
        temperature = tmp
        return temperature
    
    def getWindSpeeds(self, tmp):
        tmp = self.__getData(tmp).partition('wind_kph') #Partion unterteil ein String in 3 Bereichen. [0]= vor dem Pattern, [1] =  das Pattern selbst. [2]= nach dem Pattern
        i = tmp[2].find(':')+1 
        result = tmp[2][i:i+4].replace(',','') + ' km/h'
        return result 

    def validRequest(self,response):
        """Funktion zum Abfangen von ungültigen Städten"""
        if response != '":{"°C': 
            return True
        else:
            return False
        


WeatherAPI = HTTPRequests()
