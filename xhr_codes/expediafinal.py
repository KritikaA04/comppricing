# expedia file

import json

f = open('expedia2.json')

dataj = json.load(f)

listings = dataj['data']['flightsSearch']['listingResult']['listings']

flight_details = []

for listing in listings:
    departure_and_arrival = listing['journeys'][0]['departureAndArrivalLocations']
    duration_and_stops = listing['journeys'][0]['durationAndStops']
    price = listing['pricingInformation']['price']['completeText']
    
    # Create a dictionary for each flight
    flight = {
        "departure_and_arrival": departure_and_arrival,
        "duration_and_stops": duration_and_stops,
        "price": price
    }
    
    # Append the flight details to the list
    flight_details.append(flight)

# Display flight details
for index, flight in enumerate(flight_details, start=1):
    print(f"Flight {index}:")
    print("Departure and Arrival:", flight["departure_and_arrival"])
    print("Duration and Stops:", flight["duration_and_stops"])
    print("Price:", flight["price"])
    print()