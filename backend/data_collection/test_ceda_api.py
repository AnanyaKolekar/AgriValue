import requests

API_KEY = "786e68807c8306796b51c44a33afb40f896ff78d3ce7715f28ab0a5e95f50525"

url = "https://api.ceda.ashoka.edu.in/agmarknet/commodities"

headers = {
    "x-api-key": API_KEY,
    "Accept": "application/json"
}

try:
    response = requests.get(url, headers=headers, timeout=30)

    print("STATUS:", response.status_code)
    print("HEADERS:", dict(response.headers))
    print("RESPONSE:")
    print(response.text[:5000])

except Exception as e:
    print("ERROR:", repr(e))