import json

f = open('bookingcom.json')

data = json.load(f)
res=[]
for flightoffer in data['flightOffers']:
    breakdown_price =  flightoffer['priceBreakdown']
    total_units = breakdown_price['total'].get('units')
    if total_units is not None:
        res.append(total_units)
    
print(res)