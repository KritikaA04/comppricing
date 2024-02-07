import json

f = open('bookingcom.json')

data = json.load(f)

new_objects = []

for flight_offer in data.get("flightOffers", []):
    for segment in flight_offer.get("segments", []):
        departure_info = {
            "code": segment.get("departureAirport", {}).get("code", ""),
            "name": segment.get("departureAirport", {}).get("name", ""),
        }
        arrival_info = {
            "code": segment.get("arrivalAirport", {}).get("code", ""),
            "name": segment.get("arrivalAirport", {}).get("name", ""),
        }
        time_info = {
            "departureTime": segment.get("departureTime", ""),
            "arrivalTime": segment.get("arrivalTime", ""),
        }
        price_info = {
            # "currencyCode": flight_offer.get("priceBreakdown", {}).get("total", {}).get("currencyCode", ""),
            "units": flight_offer.get("priceBreakdown", {}).get("total", {}).get("units", 0),
            # "nanos": flight_offer.get("priceBreakdown", {}).get("total", {}).get("nanos", 0),
        }

        new_object = {
            "departureInfo": departure_info,
            "arrivalInfo": arrival_info,
            "timeInfo": time_info,
            "priceInfo": price_info,
        }

        new_objects.append(new_object)

# Display the new objects
for i, new_object in enumerate(new_objects, start=1):
    print(f"Flight {i}:\n{json.dumps(new_object, indent=4)}\n")