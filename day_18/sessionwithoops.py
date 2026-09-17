import requests

class Req:
    def __enter__(self):
        self.sess = requests.session()
        return self

    def get_r(self, url):
        self.response = self.sess.get(url)
        return self.response

    def __exit__(self, exc_type, exc, tb):
        self.sess.close()


with Req() as session:
    response1 = session.get_r("https://postman-echo.com/cookies/set?mycookie=hello")
    response2 = session.get_r("https://postman-echo.com/cookies/set?mycookie=wolrd")
    response3 = session.get_r("https://postman-echo.com/cookies")
    print(response3.text)



    