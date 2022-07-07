
import api_kiwi, api_gmaps, tool_conv
import datetime, time, math


def execute(start_location, end_location, flights, x):

  # get dateTtime from Flights object
  arrival_timedate = flights['data'][x]['local_departure']
  departure_timedate = flights['data'][x]['local_arrival']
  
  # dateTtime --> epoch
  arrival_epoch = tool_conv.datetime_to_epoch(arrival_timedate)
  departure_epoch = tool_conv.datetime_to_epoch(departure_timedate)

  # add time for stuff at the airport
  arrival_time_epoch = arrival_epoch - 4800 # 1h 20min
  departure_time_epoch = departure_epoch + 2400 # 40min
  print("Arrival time: " + str(arrival_time_epoch))

  
  
  # adjusting time for search ---------------

  current_time_epoch = time.time()

  if (arrival_time_epoch - current_time_epoch) > (7*7*86400):
    
    # ARRIVAL: searching for time from beginning of trip's day
    arrival_time_since_midnight_epoch = arrival_time_epoch%86400
    print("Arrival time since midnight: " + str(arrival_time_since_midnight_epoch))

    # DEPARTURE: searching for time from beginning of trip's day
    departure_time_since_midnight_epoch = departure_time_epoch%86400
    print("Departure time since midnight: " + str(departure_time_since_midnight_epoch))
    
    # searching for today's midnight time in epoch
    current_time_epoch = time.time()
    current_time_midnight_epoch = math.floor(current_time_epoch/86400)*86400
    print("Last midnight time: " + str(current_time_midnight_epoch))
    
    
    # ARRIVAL: searching for trip's weekday
    arrival_time_weekday = time.strftime('%A', time.localtime(arrival_time_epoch))
  
    if arrival_time_weekday == "Monday":
      arrival_time_weekday_number = 1
    elif arrival_time_weekday == "Tuesday":
      arrival_time_weekday_number = 2
    elif arrival_time_weekday == "Wednesday":
      arrival_time_weekday_number = 3
    elif arrival_time_weekday == "Thursday":
      arrival_time_weekday_number = 4
    elif arrival_time_weekday == "Friday":
      arrival_time_weekday_number = 5
    elif arrival_time_weekday == "Saturday":
      arrival_time_weekday_number = 6
    elif arrival_time_weekday == "Sunday":
      arrival_time_weekday_number = 7
    else:
      print("ERROR: arrival_time_weekday variable is wrong or unavailable")

    
    # DEPARTURE: searching for trip's weekday
    departure_time_weekday = time.strftime('%A', time.localtime(departure_time_epoch))
  
    if departure_time_weekday == "Monday":
      departure_time_weekday_number = 1
    elif departure_time_weekday == "Tuesday":
      departure_time_weekday_number = 2
    elif departure_time_weekday == "Wednesday":
      departure_time_weekday_number = 3
    elif departure_time_weekday == "Thursday":
      departure_time_weekday_number = 4
    elif departure_time_weekday == "Friday":
      departure_time_weekday_number = 5
    elif departure_time_weekday == "Saturday":
      departure_time_weekday_number = 6
    elif departure_time_weekday == "Sunday":
      departure_time_weekday_number = 7
    else:
      print("ERROR: departure_time_weekday variable is wrong or unavailable")
    
    # searching for today's weekday
    current_time_weekday = time.strftime('%A', time.localtime(current_time_epoch))
  
    if current_time_weekday == "Monday":
      current_time_weekday_number = 1
    elif current_time_weekday == "Tuesday":
      current_time_weekday_number = 2
    elif current_time_weekday == "Wednesday":
      current_time_weekday_number = 3
    elif current_time_weekday == "Thursday":
      current_time_weekday_number = 4
    elif current_time_weekday == "Friday":
      current_time_weekday_number = 5
    elif current_time_weekday == "Saturday":
      current_time_weekday_number = 6
    elif current_time_weekday == "Sunday":
      current_time_weekday_number = 7
    else:
      print("ERROR: current_time_weekday variable is wrong or unavailable")
  
    current_vs_arrival_weekday_difference = arrival_time_weekday_number - current_time_weekday_number

    current_vs_departure_weekday_difference = departure_time_weekday_number - current_time_weekday_number
  
    estimated_arrival_time_epoch = current_time_midnight_epoch + arrival_time_since_midnight_epoch + 7*7*86400 + current_vs_arrival_weekday_difference*86400

    estimated_departure_time_epoch = current_time_midnight_epoch + departure_time_since_midnight_epoch + 7*7*86400 + current_vs_departure_weekday_difference*86400

    print("Estimated arrival time: " + str(estimated_arrival_time_epoch))
    
    print("Estimated departure time: " + str(estimated_departure_time_epoch))

  else:

    estimated_arrival_time_epoch = arrival_time_epoch
    print("True arrival time: " + str(estimated_arrival_time_epoch))

    estimated_departure_time_epoch = departure_time_epoch
    print("True departure time: " + str(estimated_departure_time_epoch))

  # Remember date difference (to use for printing of results)

  estimated_vs_arrival_time_epoch =  arrival_time_epoch - estimated_arrival_time_epoch

  estimated_vs_departure_time_epoch =  departure_time_epoch - estimated_departure_time_epoch
    
  
  # call the APIs -----------------------------
  
  results_to = api_gmaps.search_simple(start_location, flights['data'][x]['flyFrom'] + " airport", estimated_arrival_time_epoch, True)

  if results_to['status'] != 'OK':
      results_to = api_gmaps.search_simple(start_location, flights['data'][x]['cityFrom'] + " airport", estimated_arrival_time_epoch, True)
  
  results_from = api_gmaps.search_simple(flights['data'][x]['flyTo'] + " airport", end_location, estimated_departure_time_epoch, False)
  
  if results_from['status'] != 'OK':
    results_from = api_gmaps.search_simple(flights['data'][x]['cityTo'] + " airport", end_location, estimated_departure_time_epoch, False)
    
  return results_to, results_from, estimated_vs_arrival_time_epoch, estimated_vs_departure_time_epoch