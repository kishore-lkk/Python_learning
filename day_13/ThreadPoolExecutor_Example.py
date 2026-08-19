from concurrent.futures import ThreadPoolExecutor
import time 
import requests
import json 

# Threads using submit
"""
def dummy_function():
    time.sleep(5)

starting_time = time.time()

print("started")
for i in range(3):
    dummy_function()
ending_time = time.time()
print(f"The time taken to complete the script without threading is {ending_time - starting_time}")

print("started with threading")
starting_time = time.time()
with ThreadPoolExecutor(3) as executor:
    for i in range(3):
        work = executor.submit(dummy_function)
ending_time = time.time()
print(f"the time taken to complete the function calling with thread is {ending_time - starting_time}")
"""

# Threads using map

def status_fetcher(input):
    status = requests.get(input, timeout=5).status_code
    return(status)


result = {}
with open("Learning/day_13/input.txt", "r", encoding="utf-8") as rf:
    url_list = json.load(rf)


start_time = time.time()
print("Started without using threads")
for url in url_list:
    result.update({url : status_fetcher(url)})
print(f"{result}, time taken is {time.time() - start_time}") 

start_time = time.time()
print("started with threading using map")
with ThreadPoolExecutor() as executor:
    status_list = list(executor.map(status_fetcher, url_list))
    result = dict(zip(url_list,status_list))
print(f"{result}, the time taken with threading is {time.time() - start_time}")


# the below method is not working, as "future.result()" is making the other threads to stop 
"""
start_time = time.time()
print("started with threading using submit")
with ThreadPoolExecutor() as executor:
    for url in url_list:
        future = executor.submit(status_fetcher, url) 
        result.update({url : future.result()})
print(f"{result}, the time taken with threading is {time.time() - start_time}")
"""