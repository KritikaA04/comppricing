from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=chrome_options)

dev_tools = driver.execute_cdp_cmd("Network.enable", {})
dev_tools = driver.execute_cdp_cmd("Network.enable", {})

def request_will_be_sent(request):
    print(request['params']['request']['url'])

def response_received(response):
    request_id = response['params']['requestId']
    response_data = response['params']['response']
    
    if 'ws_api.php?' in response_data['url']:
        print(response_data['status'], response_data['url'])
        assert response_data['status'] == 200
        response_body = dev_tools.execute_cdp_cmd("Network.getResponseBody", {'requestId': request_id})
        print(response_body['body'])

dev_tools.on("Network.requestWillBeSent", request_will_be_sent)
dev_tools.on("Network.responseReceived", response_received)

driver.get("https://weatherstack.com/")
