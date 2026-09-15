import requests

response = requests.session()
# Step 1: Set a cookie
r1 = response.get("https://postman-echo.com/cookies/set?mycookie=hello")
print("Response headers:", r1.headers.get("Set-Cookie"))

# Step 2: Fetch cookies back
r2 = response.get("https://postman-echo.com/cookies")
print("Cookies returned:", r2.json())