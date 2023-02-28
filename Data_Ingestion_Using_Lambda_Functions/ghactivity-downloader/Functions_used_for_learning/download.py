import requests


def download_file(file):
    resp = requests.get(f'https://data.gharchive.org/{file}')
    return resp


res = download_file('2021-01-29-0.json.gz')

print(res.status_code)
