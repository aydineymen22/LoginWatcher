import requests

def get_location():
    try:
        response = requests.get("https://ipinfo.io/json", timeout=5)
        data = response.json()

        location_info = {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "org": data.get("org")
        }

        return location_info

    except Exception as e:
        return {"error": str(e)}
