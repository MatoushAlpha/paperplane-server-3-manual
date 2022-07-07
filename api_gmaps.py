
import requests, os
import tool_conv, tool_debug

key_gmaps = os.environ['api_key_gmaps']


def search_simple(start_location, end_location, time_epoch, travel_to_true):

  # Construct URL --------
  
  if travel_to_true is True:
    URL = "https://maps.googleapis.com/maps/api/directions/json?mode=transit&origin=" + start_location + "&destination=" + end_location + "&arrival_time=" + str(time_epoch) + "&key=" + key_gmaps
    
  elif travel_to_true is False:
    URL = "https://maps.googleapis.com/maps/api/directions/json?mode=transit&origin=" + start_location + "&destination=" + end_location + "&departure_time=" + str(time_epoch) + "&key=" + key_gmaps

  # Error-handling for travel_to_true
  else:
    print("ERROR: In api_gmaps.py -> travel_to_true is unspecified, couldn't call API")

  # Print and log URL into debug
  print(URL)
  tool_debug.log_nl()
  tool_debug.log_add("Google Maps API URL called: " + URL)
  tool_debug.log_nl()
    
  # Call API ----------
  response = requests.get(URL)
  response = response.json()

  # Checking results
  print("Google Maps found " + str(len(response["routes"])) + " routes")

  # Return
  return response
  