import requests

API_KEY = "4c3f385c39d9841395acd55e78fc66ec"


def get_data(place, forecast_days=1, kind="Temperature"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code}")
    data = response.json()

    filtered_data = data["list"]
    nr_values = 8 * forecast_days  # 8 data points per day (3-hour intervals)
    filtered_data = filtered_data[:nr_values]

    dates = [entry["dt_txt"] for entry in filtered_data]

    if kind == "Temperature":
        # Convert from Kelvin to Celsius
        values = [entry["main"]["temp"] - 273.15 for entry in filtered_data]
    elif kind == "Sky":
        values = [entry["weather"][0]["main"] for entry in filtered_data]
    else:
        raise ValueError("Invalid kind specified. Use 'Temperature' or 'Sky'.")

    return dates, values


if __name__ == "__main__":
    place = "tokyo"
    forecast_days = 3
    kind = "Temperature"  # or "Sky"

    try:
        data = get_data(place, forecast_days, kind)
        print(data)
    except Exception as e:
        print(e)
