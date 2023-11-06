import keys, requests, json

five_minute_bar_url = keys.BARS_URL + "/5Min?symbols=SPX" #5 minute bar
ten_minute_bar_url = keys.BARS_URL + "/10Min?symbols=SPX" #10 minute bar

#get 5 minute bar
r = requests.get(five_minute_bar_url, headers=keys.HEADERS)
print(json.dumps(r.json(), indent=4))