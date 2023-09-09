import requests
import config


response = requests.get(
  'https://api.stormglass.io/v2/tide/extremes/point',
  params={
    'lat': config.lat,
    'lng': config.lng,
  },
  headers={
    'Authorization': config.api_key
  }
)

# Do something with response data.
json_data = response.json()

print("Next tide")
print (json_data["data"][:8])


print("\n Meta data on request")
print (json_data["meta"])