import requests

url = "https://flights.booking.com/api/flights/?type=ONEWAY&adults=1&cabinClass=ECONOMY&children=&from=BOM.AIRPORT&to=DEL.AIRPORT&fromCountry=IN&toCountry=IN&fromLocationName=Chhatrapati+Shivaji+International+Airport+Mumbai&toLocationName=Delhi+International+Airport&depart=2024-02-15&sort=BEST&travelPurpose=leisure&aid=2311236&label=en-in-booking-desktop-CmH43mrsjzqEEFQPgVycoAS652796016141%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9146601%3Ali%3Adec%3Adm&enableVI=1&enableDiscounts=cug"

payload = {}
headers = {
  'authority': 'flights.booking.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'px_init=0; bkng_sso_auth=CAIQsOnuTRpmbFzIl9vdisMB943ZZkQBOF8S6gdzdugYaxAQE89qrwx0J/ACth6YgvGRwOKebZL3v9FL+kEYEPD0JJnL1Lof4IMVwgk3Z3EbZKwiVzBKy5k5uKUUCNz32EaHa7zqpiMi87FK6xg/; pcm_consent=analytical%3Dtrue%26countryCode%3DIN%26consentId%3D2f02fb37-59c3-4fa5-b4a1-2833bbe6715e%26consentedAt%3D2024-02-04T07%3A29%3A16.291Z%26expiresAt%3D2024-08-02T07%3A29%3A16.291Z%26implicit%3Dtrue%26marketing%3Dtrue%26regionCode%3DMP%26regulation%3Dnone%26legacyRegulation%3Dnone; cors_js=1; BJS=-; _gid=GA1.2.5168548.1707031760; _gac_UA-116109-18=1.1707031760.Cj0KCQiA5fetBhC9ARIsAP1UMgHu2glTO4e0OsdUyW9xQ0S3f3jJsIunD2IlizOEROREkEn-TrzTdKYaApH0EALw_wcB; bkng_sso_ses=e30; bkng_sso_session=e30; bkng_prue=1; _gcl_au=1.1.313768681.1707031761; _gcl_aw=GCL.1707031762.Cj0KCQiA5fetBhC9ARIsAP1UMgHu2glTO4e0OsdUyW9xQ0S3f3jJsIunD2IlizOEROREkEn-TrzTdKYaApH0EALw_wcB; _ga=GA1.1.1107600318.1707031760; _scid=10745ca4-c6e5-42d7-a3c6-428226c1aa02; _scid_r=10745ca4-c6e5-42d7-a3c6-428226c1aa02; FPID=FPID2.2.mX5E2IoBidAoZ8wO%2FjHkrHwwCnYN8kBB9uXyvKETt9c%3D.1707031760; FPLC=fbSjgXOo%2BCGjurrwARMDpADJydKlh%2Fqs2NZzflI5Wuuw0CfwTc%2BqvASOzDIZyOge9sR63ZJApSR4itewlKZ40ZYpylNaB72333zcJYC5tmySrCI3iFgku2%2FFaGsCUg%3D%3D; _pin_unauth=dWlkPU1HWmlPRGs0WVRndFpUY3dOQzAwTUdZMUxUZzRZMlV0TkdJd05HTmpOR0k1WXpJMA; _sctr=1%7C1706985000000; fasc=f479e94c-dd9b-4070-a2e0-85fee336d2cc; pc_payer_id=98b15e70-58dc-4e49-8941-3dc9b8025f79; fsc=s%3A5e0163bb512c2528b4beef6f5cd5ab16.dWbtH8X7t3FanQjpzJg9d8qOVqMUHRedtYGaUNnq4Nw; _ga_FPD6YLJCJ7=GS1.1.1707031762.1.1.1707031982.58.0.0; _ga_A12345=GS1.1.1707031762.1.1.1707031982.0.0.0; lastSeen=1707031982860; fsc=s%3A5e0163bb512c2528b4beef6f5cd5ab16.dWbtH8X7t3FanQjpzJg9d8qOVqMUHRedtYGaUNnq4Nw; OptanonConsent=implicitConsentCountry=nonGDPR&implicitConsentDate=1707031761371; _uetsid=1de36880c32f11ee958e398941a97f5d; _uetvid=1de37ec0c32f11ee9eb4e77d91f83da0; bkng=11UmFuZG9tSVYkc2RlIyh9YWIKSswmuZ6U7L1PX%2BvEdqFyPM9clyve%2B7Bh981cISwbW2cEWYTWw51d4kRsqHnHUZ%2F4cB1%2BLzvKeneULhAY3Wt0aF9BvMCTj%2BD92q1kfsEC%2BDs0tymf5kWJ%2B2S2UY80tBcKzgK5fIVMdZKEwU%2Ba0TZ4H9eZFJ3FFSQphEBJxvarFNXsrwp4ksM%3D; fasc=f479e94c-dd9b-4070-a2e0-85fee336d2cc; fsc=s%3A5e0163bb512c2528b4beef6f5cd5ab16.dWbtH8X7t3FanQjpzJg9d8qOVqMUHRedtYGaUNnq4Nw',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'x-booking-affiliate-id': '2311236',
  'x-booking-flights-client-hints': 'price_change_v2',
  'x-booking-label': 'en-in-booking-desktop-CmH43mrsjzqEEFQPgVycoAS652796016141:pl:ta:p1:p2:ac:ap:neg:fi:tikwd-65526620:lp9146601:li:dec:dm',
  'x-booking-parent-request-id': '12ea5fcf-8b4c-4202-83e1-3f1f5280bfd1',
  'x-booking-request-tree-id': '12ea5fcf-8b4c-4202-83e1-3f1f5280bfd1',
  'x-booking-trace-meta': 'caller_persona="b-flights-frontend"; root_caller_persona="b-flights-frontend"',
  'x-flights-context-name': 'search_results',
  'x-requested-from': 'clientFetch'
}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)


data =  response.json()
for airline in data['airlines']:
    flight_amount= airline['minPrice'].get('units')
    if flight_amount is not None:
        res.append(flight_amount)
 
print(res)