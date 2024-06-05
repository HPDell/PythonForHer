from pathlib import Path
from urllib3 import request

MY_KEY = (Path(__file__).parent / "key_amap.txt").read_text().strip()
GET = "GET"
BASE_URL = 'https://restapi.amap.com/v3/place/text'
BASE_QS = {
  'key': MY_KEY,
  'types': '150900',
  'city': '0371',
  'citylimit': True,
  'offset': 20
}

def get_page(page):
  resp = request(GET, BASE_URL, fields={
    **BASE_QS,
    'page': page
  })
  if resp.status == 200:
    res = resp.json()
    if res['status'] == "1":
      total_count = res['count']
      pois = res['pois']
      return (total_count, pois)
    else:
      raise ValueError("Response status is zero", res['info'])
  else:
    raise ValueError("Request failed", resp.status)

print(get_page(1))
