import requests

API_KEY = "4c3f385c39d9841395acd55e78fc66ec"

def get_data(place,days=None, option=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__=="__main__":
    print(get_data(place="tokyo"))