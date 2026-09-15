import requests

class Req:
    def __init__(self):
        self.req = requests.session()
        pass
    def get_request(self, arg):
        response = self.req.get(arg)
        return response



requester = Req()
resp1 =requester.get_request("https://postman-echo.com/cookies/set?mycookie=hello")
resp2 =requester.get_request("https://postman-echo.com/cookies/set?mycookie=world")
resp3 =requester.get_request("https://postman-echo.com/cookies")

print(resp3.json())

