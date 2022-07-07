import datetime
import tool_debug
from geopy.geocoders import Nominatim

def datetime_to_epoch(arrival):

  tool_debug.log_add("datetime_to_epoch function:")
  tool_debug.log_add("parameters:" + str(arrival))
  
  datetime_list = arrival.split('T')
  date_list = datetime_list[0].split('-')
  time_list = datetime_list[1].split('.')
  time_list = time_list[0].split(':')

  for x in range(3):
    date_list[x] = int(date_list[x])

  for x in range(3):
    time_list[x] = int(time_list[x])

  epoch = datetime.datetime(date_list[0], date_list[1], date_list[2], time_list[0], time_list[1], time_list[2]).timestamp()

  epoch = str(epoch).split(".")
  epoch[0] = int(epoch[0])

  #tool_debug.log_add(epoch[0])
  #tool_debug.log_nl()

  return epoch[0]

def geocoding(location):

  geolocator = Nominatim(user_agent="paperplane")
  location = geolocator.geocode(location)

  latitude = location.latitude
  longitude = location.longitude
  
  geocode = {
    'lat': latitude,
    'lon': longitude
  }
  
  return geocode

def geocoding_kiwi(location):

  geolocator = Nominatim(user_agent="paperplane")
  location = geolocator.geocode(location)

  latitude = location.latitude
  longitude = location.longitude

  formatted_string = "{:.2f}".format(latitude)
  latitude = float(formatted_string)

  formatted_string = "{:.2f}".format(longitude)
  longitude = float(formatted_string)
  
  geocode = {
    'lat': latitude,
    'lon': longitude
  }
  
  return geocode
def reduce_geocode_for_kiwi(number):

  print(type(number))

  formatted_string = "{:.2f}".format(number)
  number = float(formatted_string)

  return number


def arrive_earlier_by_10m(string_arrival, counts):

  arrival_time = list(string_arrival)

  counter = 0
  
  while counter < counts:
    
    if int(arrival_time[14]) == 0:
      if int(arrival_time[12]) == 0:
        if int(arrival_time[11]) == 0:
          arrival_time[9] = str(int(arrival_time[9])-1)
          arrival_time[11] = "2"
          arrival_time[12] = "3"
          arrival_time[14] = "5"
        elif int(arrival_time[11]) == 2:
          arrival_time[11] = "1"
          arrival_time[12] = "9"
          arrival_time[14] = "5"
        elif int(arrival_time[11]) == 1:
          arrival_time[11] = "0"
          arrival_time[12] = "9"
          arrival_time[14] = "5"
      else:
        arrival_time[12] = str(int(arrival_time[12])-1)
        arrival_time[14] = "5"
    else:
      arrival_time[14] = str(int(arrival_time[14])-1)

    counter += 1
  
  string_arrival = "".join(arrival_time)                        
  return string_arrival

def depart_later_by_10m(string_arrival, counts):

  arrival_time = list(string_arrival)

  counter = 0
  
  while counter < counts:
    if int(arrival_time[14]) == 5:
      if int(arrival_time[11]) == 2 and int(arrival_time[12]) == 3:
        arrival_time[11] = "0"
        arrival_time[12] = "0"
        arrival_time[14] = "0"
        arrival_time[9] = str(int(arrival_time[9])+1)
      elif int(arrival_time[11]) == 1:
        arrival_time[11] = "2"
        arrival_time[12] = "0"
        arrival_time[14] = "0"
      elif int(arrival_time[11]) == 0:
        arrival_time[11] = "1"
        arrival_time[12] = "0"
        arrival_time[14] = "0"
      else:
        arrival_time[14] = "0"
        arrival_time[12] = str(int(arrival_time[12])+1)
    else:
      arrival_time[14] = str(int(arrival_time[14])+1)

    counter += 1
  
  string_arrival = "".join(arrival_time)                        
  return string_arrival

  