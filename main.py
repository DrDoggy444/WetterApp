import UI
import API_calls

UI.startUp()
print(API_calls.REQUEST.CheckOnlineStatus())
UI.okOnClick(args =UI.getInput(),method= API_calls.REQUEST.getCurrentWeather()) 