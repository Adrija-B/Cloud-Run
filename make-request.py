import requests

# ~~~ make-request.py ~~~

# route 1 -- ping
def call_ping_route():
  r = requests.get('http://localhost:5000/ping')
  return r

# route 2 -- random word
def call_random_word_route():
  r = requests.get('http://localhost:5000/word')
  return r

# route 3 -- string count
def call_string_count():
  r = requests.post("http://localhost:5000/string-count",json ='adrija')
  return r


route_callers = [
  call_ping_route,
  call_random_word_route,
  call_string_count
  ]

for call_route in route_callers:
  r = call_route()
  r.status_code
  data = r.json()
  print(data) # print the response
