from datetime import datetime as dt
from datetime import timedelta as td
import requests

next_file = '2023-02-22-0.json.gz'

while True:
    res = requests.get(f'https://data.gharchive.org/{next_file}')
    if res.status_code != 200:
        break
    print(f'The status code for {next_file} is {res.status_code}')
    dt_part = next_file.split('.')[0]
    next_file = f"{dt.strftime(dt.strptime(dt_part, '%Y-%M-%d-%H') + td(hours=1), '%Y-%M-%d-%-H')}.json.gz"

