import requests
import datetime
import json

# 현재 날짜와 시간을 가져오기
now = datetime.datetime.now()

# 날짜와 시간을 API 요청 형식에 맞추기
base_date = now.strftime('%Y%m%d')  # 형식: YYYYMMDD
base_time = now.strftime('%H00')  # 형식: HHMM (정시 기준으로 요청, 예: 0600)

# API 요청 URL 및 매개변수 설정
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params = {
    'serviceKey': 'YwC1dSmoNw21NSZoAmyc55py8z1TutAqgJ5hcJFFhtqFPtXo++NZB57dNtpxitOAA+GAlGlPFGWMfTbi7epGTQ==',
    'pageNo': '1',
    'numOfRows': '1000',
    'dataType': 'JSON',
    'base_date': base_date,
    'base_time': base_time,
    'nx': '55',
    'ny': '127'
}

# API 요청 보내기
response = requests.get(url, params=params)

print("=== response json data start ===")
print(response)
print("=== response json data end ===")
print()

r_dict = json.loads(response.text)
r_response = r_dict.get("response")
r_body = r_response.get("body")
r_items = r_body.get("items")
r_item = r_items.get("item")

result = {}
for item in r_item:
    if(item.get("category") == "T1H"):
        result = item
        break
print("==== response dictionary(python object) data start ===")
print(r_dict)
print("==== response dictionary(python object) data end ===")
print()

