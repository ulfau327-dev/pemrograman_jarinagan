import requests

def get_weather(city_name, lat, lon):
    print(f"\n--- Mengambil Data Cuaca untuk {city_name} ---")

    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        'latitude': lat,
        'longitude': lon,
        'current_weather': 'true',
        'timezone': 'auto'
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            current = data['current_weather']

            suhu = current['temperature']
            kecepatan_angin = current['windspeed']

            print(f"🌡️  Suhu Saat Ini: {suhu}°C")
            print(f"💨 Kecepatan Angin: {kecepatan_angin} km/h")
            print(f"🌍 Koordinat: {lat}, {lon}")
        else:
            print(f"[ERROR] Status code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("[ERROR] Tidak ada koneksi internet!")
    except requests.exceptions.Timeout:
        print("[ERROR] Request timeout (koneksi lambat)")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    get_weather("Manado", 1.4748, 124.8421)
    get_weather("Makassar", -5.1477, 119.4327)