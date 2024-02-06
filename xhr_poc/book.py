import requests

url = "https://flights.booking.com/api/search/min-price/?type=ONEWAY&adults=1&cabinClass=ECONOMY&children=&from=BOM.AIRPORT&to=DEL.AIRPORT&fromCountry=IN&toCountry=IN&fromLocationName=Chhatrapati+Shivaji+International+Airport+Mumbai&toLocationName=Delhi+International+Airport&depart=2024-02-15&sort=BEST&travelPurpose=leisure&aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4Apr87a0GwAIB0gIkMjRlMDgxOGYtY2UzMC00MzE1LWI2ZmYtMWM3OTA4OThlZjg42AIF4AIB&enableVI=1&enableDiscounts=cug&useAggregateCache=1&compareBestPrice=1"

payload = {}
headers = {
  'authority': 'flights.booking.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'px_init=0; cors_js=1; bkng_sso_session=e30; bkng_sso_ses=eyJib29raW5nX2dsb2JhbCI6W3siYSI6MSwiaCI6Im90SVlBN2tGbDZvenhLY0s4MDRBa1ZQWWJVL2piRGFyVndJK1gzeGhIbkkifV19; pcm_consent=consentedAt%3D2024-01-30T15%3A38%3A04.870Z%26countryCode%3DIN%26expiresAt%3D2024-07-28T15%3A38%3A04.870Z%26implicit%3Dfalse%26regionCode%3DMP%26regulation%3Dnone%26legacyRegulation%3Dnone%26consentId%3D519194c4-4cc0-4232-8fee-f1e33c7777e9%26analytical%3Dtrue%26marketing%3Dtrue; bkng_sso_auth=CAIQsOnuTRpmL3cH+JtIQPF2VKOD3mml1uwMHDKbnB0OZQj5q53Lo0yHYWB1ejCOGtjncrcHT1APyFh/dWFQXt/SLdtYzV2FVIUZJmCLR/2cW07nZwpVQd5k02OY7kpxrw51K4X7imIJSX0kYL06; _gid=GA1.2.1380073122.1706786332; BJS=-; bkng_prue=1; _gcl_au=1.1.1638433861.1706786332; _scid=3cec66be-cb02-4a4c-8cde-4ad2d99a6474; _scid_r=3cec66be-cb02-4a4c-8cde-4ad2d99a6474; _ga=GA1.1.1811717328.1706786332; _sctr=1%7C1706725800000; _pin_unauth=dWlkPU56a3paakUxTmpFdE0yVmhNaTAwWXpjeExUazBOVGt0TXpreVlqSTFNamd4TkdRMQ; FPID=FPID2.2.6kJFVNF0j9GowSytcsU%2F%2B6feozIvJlIfF9mS9srtb7g%3D.1706786332; FPLC=EtoTT6rzOrQcZApoOcomeC78dEcf2c3Qf1q2G5ElgIsM8DLSCs0jWj1bCuSRoEjXSci50U6olGOVF1F0%2F1g%2FrTTxZbC9EMM%2FzLvypCTo%2FHS%2FXXnOJbj27qIJ%2BjiD%2Bw%3D%3D; fasc=efba06ee-ac58-4ba1-873a-5afa687d69df; pc_payer_id=45dffe22-0c0b-4d60-9220-386382b46e3a; fsc=s%3Ab0337dbfeb5561de1b0cdb0f47a28a81.4sQd4DGMtYMj5RrhZuU7i9atydEleqyDEQ2uMRHXPA4; _ga_FPD6YLJCJ7=GS1.1.1706786332.1.1.1706786572.57.0.0; _ga_A12345=GS1.1.1706786332.1.1.1706786572.0.0.0; lastSeen=1706786572110; fsc=s%3Ab0337dbfeb5561de1b0cdb0f47a28a81.4sQd4DGMtYMj5RrhZuU7i9atydEleqyDEQ2uMRHXPA4; OptanonConsent=implicitConsentCountry=nonGDPR&implicitConsentDate=1706628303509; _uetsid=ae260860c0f311ee8a6e032493d73f34; _uetvid=ae263de0c0f311eeb710095961cfef19; bkng=11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLblgO%2Fz4BDP5vZoF4O%2BTHbgf3NaiwsovWTvo7Ja8cRiqTGFakCMx39DHrj%2FyOCSfe3mG4EMrplfbjKqln0m0cO98GbQou8twT1wUf0A35zn66qxgQl9bJxfR5HJltItfnXuMkCU8Opx5KZMDCAgymwl0s7ypbhhR9kqPSaRnFz8Mw%3D; fasc=efba06ee-ac58-4ba1-873a-5afa687d69df; fsc=s%3Ab0337dbfeb5561de1b0cdb0f47a28a81.4sQd4DGMtYMj5RrhZuU7i9atydEleqyDEQ2uMRHXPA4',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'x-booking-affiliate-id': '304142',
  'x-booking-flights-client-hints': 'price_change_v2',
  'x-booking-label': 'gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4Apr87a0GwAIB0gIkMjRlMDgxOGYtY2UzMC00MzE1LWI2ZmYtMWM3OTA4OThlZjg42AIF4AIB',
  'x-booking-parent-request-id': 'acf9df33-3c34-47f7-96c4-26e07ac31280',
  'x-booking-request-tree-id': 'acf9df33-3c34-47f7-96c4-26e07ac31280',
  'x-booking-trace-meta': 'caller_persona="b-flights-frontend"; root_caller_persona="b-flights-frontend"',
  'x-flights-context-name': 'search_results',
  'x-requested-from': 'clientFetch'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)


data = response.json()

