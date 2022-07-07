
import api_kiwi, api_gmaps, pp_ground, tool_results, tool_debug
import datetime, math
from time import strftime
from time import gmtime


def execute(start_location, end_location, min_date, max_date, number_of_results, display_details):

  #load flights
  flights = api_kiwi.search(start_location, end_location, min_date, max_date, 250, number_of_results)

  # RESTART DEBUG AND RESULT LOGS
  tool_results.log_restart()
  tool_debug.log_restart() 

  # LOG THE SEARCH QUERY PARAMETERS 
  tool_results.log_nl()
  tool_results.log_add("SEARCH")
  tool_results.log_nl()
  tool_results.log_add("Start location: " + start_location)
  tool_results.log_add("End location: " + end_location)
  tool_results.log_add("Date range: " + min_date + "-" + max_date)
  tool_results.log_nl()
  tool_results.log_add("------------------")
  tool_results.log_nl()
  
  # Go through each flight result
  for x in range(len(flights['data'])):
    
    #find ground transport
    ground = pp_ground.execute(start_location, end_location, flights, x)


    # DEBUGGING LOGS


    tool_debug.log_nl()
    tool_debug.log_add("Result " + str(x+1) + " -------------")
    tool_debug.log_nl()
    # JSON with ground transport to the airport:
    tool_debug.log_add(ground[0]) 
    tool_debug.log_nl()
    tool_debug.log_nl()
    tool_debug.log_nl()
    # JSON with the flight data:
    tool_debug.log_add(flights) 
    tool_debug.log_nl()
    tool_debug.log_nl()
    tool_debug.log_nl()
    # JSON with ground transport from the airport:
    tool_debug.log_add(ground[1]) 
    tool_debug.log_nl()
    tool_debug.log_nl()
    tool_debug.log_nl()


    
    # PRINTING RESULTS

    tool_results.log_nl()
    tool_results.log_add("Result " + str(x+1) + " -------------")
    tool_results.log_nl()

    # If both Gmaps API calls were succesfull:
    if ground[0]['status'] == 'OK' and ground[1]['status'] == 'OK':

      # General information (departure datetime, arrival datetime, airports, price of the flight):
      
      tool_results.log_add("Departure " + str(datetime.datetime.fromtimestamp(ground[0]['routes'][0]['legs'][0]['departure_time']['value'] + ground[2])) + " UTC")
      tool_results.log_add("Arrival " + str(datetime.datetime.fromtimestamp(ground[1]['routes'][0]['legs'][0]['arrival_time']['value'] + ground[3])) + " UTC")

    # Tried estimating the duration od the journey (TBD):
      #duration_in_seconds = ground[1]['routes'][0]['legs'][0]['arrival_time']['value'] - ground[0]['routes'][0]['legs'][0]['departure_time']['value']
      #tool_results.log_add("Duration: " + str(math.floor(duration_in_seconds/86400)) + "days" + str(strftime("%H hrs %M min", gmtime(duration_in_seconds))))
      
    tool_results.log_add("Flying through: " + flights['data'][x]['cityFrom'] + " " + flights['data'][x]['flyFrom'] + " and " + flights['data'][x]['cityTo'] + " " + flights['data'][x]['flyTo'])
    tool_results.log_add("Cost of the airplane ticket: " + str(flights['data'][x]['conversion']['EUR']) + "EUR")
    tool_results.log_nl()

    
    # Information about the transport to the airport
    
    tool_results.log_add("Transport to the airport:")
    if ground[0]['status'] != 'OK':
      tool_results.log_add("Couldn't find transportation to the airport for this flight.")
      tool_results.log_nl()

    elif display_details is True:
      counter = 1
      for z in range(len(ground[0]['routes'][0]['legs'][0]['steps'])):
        if ground[0]['routes'][0]['legs'][0]['steps'][z]['travel_mode'] == "TRANSIT":
          tool_results.log_add("  " + str(counter) + " - " + ground[0]['routes'][0]['legs'][0]['steps'][z]['transit_details']['departure_time']['text'] + " - " + ground[0]['routes'][0]['legs'][0]['steps'][z]['transit_details']['departure_stop']['name'] + " - " + ground[0]['routes'][0]['legs'][0]['steps'][z]['transit_details']['line']['agencies'][0]['name'] + " (" + ground[0]['routes'][0]['legs'][0]['steps'][z]['transit_details']['line']['vehicle']['name'] + ")")
          counter += 1
      

    # Information about the transport from the airport:
          
    tool_results.log_nl()
    tool_results.log_add("Transport from the airport:")
    if ground[1]['status'] != 'OK':

      tool_results.log_add("Couldn't find transportation from the airport for this flight.")
      tool_results.log_nl()

    elif display_details is True:
      counter = 1
      for z in range(len(ground[1]['routes'][0]['legs'][0]['steps'])):
        if ground[1]['routes'][0]['legs'][0]['steps'][z]['travel_mode'] == "TRANSIT":
          tool_results.log_add("  " + str(counter) + " - " + ground[1]['routes'][0]['legs'][0]['steps'][z]['transit_details']['departure_time']['text'] + " - " + ground[1]['routes'][0]['legs'][0]['steps'][z]['transit_details']['departure_stop']['name'] + " - " + ground[1]['routes'][0]['legs'][0]['steps'][z]['transit_details']['line']['agencies'][0]['name'] + " (" + ground[1]['routes'][0]['legs'][0]['steps'][z]['transit_details']['line']['vehicle']['name'] + ")")
          counter += 1

    tool_results.log_nl()




    

