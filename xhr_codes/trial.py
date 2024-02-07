import json

f = open('bookingcom.json')
data = json.load(f)

new_objects = []

for flight_offer in data.get("flightOffers", []):
    for segment in flight_offer.get("segments", []):
        departure_info = segment.get("departureAirport", {}).get("name", "")
        arrival_info = segment.get("arrivalAirport", {}).get("name", "")
        departure_code = segment.get("departureAirport", {}).get("code", "")
        arrival_code = segment.get("arrivalAirport", {}).get("code", "")
        departure_time = segment.get("departureTime", "")
        arrival_time = segment.get("arrivalTime", "")
        price = flight_offer.get("priceBreakdown", {}).get("total", {}).get("units", 0)

        new_object = {
            "departure_info": departure_info,
            "arrival_info": arrival_info,
            "departure_code": departure_code,
            "arrival_code": arrival_code,
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "price": price
        }

        new_objects.append(new_object)

# Display the new objects
for i, new_object in enumerate(new_objects, start=1):
    print(f"Flight {i}:")
    print("Departure and Arrival:", new_object["departure_info"], f"({new_object['departure_code']}) -", new_object["arrival_info"], f"({new_object['arrival_code']})")
    print("Departure Time:", new_object["departure_time"])
    print("Arrival Time:", new_object["arrival_time"])
    print("Price:", new_object["price"])
    print()
