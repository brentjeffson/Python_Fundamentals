import base64
import requests
import time

credentials = (base64.b64encode(b'user'), base64.b64encode(b'admin'))
login_api = 'http://192.168.254.254/goform/goform_set_cmd_process'
print(credentials)

payload = {
    'isTest': 'false',
    'goformId': 'LOGIN',
    'username': str(base64.b64encode(b'user')),
    'password': str(base64.b64encode(b'admin')),
}
# login
print(type(base64.b64encode(b'user')))
s = requests.Session()
resp = s.post(login_api, data=payload)
print(resp.status_code)
print(resp.text)

# fetch messages
params = {
    '_': str(round(time.time() * 1000)),
    'isTest': 'false',
    'cmd': 'sms_data_total',
    'page': '0',
    'data_per_page': '500',
    'mem_store': '1',
    'tags': '10',
    'order_by': 'order by id desc',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fil;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '69',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'pageForward=home',
    'Host': '192.168.254.254',
    'Origin': 'http',
    'Referer': 'http',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
resp = s.get('http://192.168.254.254/goform/goform_get_cmd_process', headers=headers, params=params)
print(resp.status_code)

print(resp.headers)
print(resp.request.headers)
with open('sms.json', 'wt') as f:
    f.write(resp.text)
    print(resp.json)