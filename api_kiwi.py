
import requests, os
import tool_conv
key_kiwi = os.environ['api_key_kiwi']

def search(start_location, end_location, start_date, end_date, radius, results_number):


  #process input data
  #geocoding
  start_geocode = tool_conv.geocoding_kiwi(start_location)
  end_geocode = tool_conv.geocoding_kiwi(end_location)  

  #base URL  
  URL_base = "https://tequila-api.kiwi.com/v2/search?"

  #state URL components
  URL_flyFrom = "fly_from=" + str(start_geocode["lat"]) + "-" + str(start_geocode["lon"]) + "-" + str(radius) + "km"
  URL_flyTo = "fly_to=" + str(end_geocode["lat"]) + "-" + str(end_geocode["lon"]) + "-" + str(radius) + "km"
  URL_dateFrom = "dateFrom=" + start_date
  URL_dateTo = "dateTo=" + end_date
  URL_results = "limit=" + str(results_number)

  #assemble URL
  URL = URL_base + URL_flyFrom + "&" + URL_flyTo + "&" + URL_dateFrom + "&" + URL_dateTo + "&" + URL_results

  #check URL in console
  print(URL)
  
  #call API with URL
  response = requests.get(URL, headers = {'apikey': key_kiwi})

  #process API data
  response = response.json()

  print("Kiwi.com flights search succesfull")
  
  return response
