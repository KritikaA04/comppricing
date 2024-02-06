import json

f = open('expedia2.json')

data = json.load(f)
# formatted_prices = []

# # Extract formatted prices from Stops
# stops_options = data["data"]["flightsSearch"]["sortAndFilterResult"]["filterPresentation"]["options"][0]["items"]
# for stop_option in stops_options:
#     formatted_prices.append(stop_option["startingPrice"]["formatted"])

# # Extract formatted prices from Airlines
# airlines_options = data["data"]["flightsSearch"]["sortAndFilterResult"]["filterPresentation"]["options"][1]["items"]
# for airline_option in airlines_options:
#     formatted_prices.append(airline_option["startingPrice"]["formatted"])

# # Print the extracted formatted prices
# for price in formatted_prices:
#     print(price)


formatted_prices = []

# Extract all formatted prices
filter_options = data["data"]["flightsSearch"]["sortAndFilterResult"]["filterPresentation"]["options"]
for option in filter_options:
    for item in option.get("items", []):
        starting_price = item.get("startingPrice", {}).get("formatted")
        if starting_price:
            formatted_prices.append(starting_price)

# Print the extracted formatted prices
for price in formatted_prices:
    print(price)