from requests.auth import HTTPBasicAuth
import requests

s = requests.Session()
# s.auth = HTTPBasicAuth('brentjeffson', '061798@kaizen')

payload = {
    'reg_username': 'brentjeffson',
    'reg_password': '061798@kaizen',
    'chk_rememberme': '1'
}

resp = s.post('https://www.scribblehub.com/login', data=payload)
# print(resp.status_code)

resp = s.get('https://www.scribblehub.com/favorites/')


with open('Requests/html.html', 'wt') as f:
    f.write(resp.text)