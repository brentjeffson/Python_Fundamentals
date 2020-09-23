raw_headers = """
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fil;q=0.8
Connection: keep-alive
Content-Length: 69
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: pageForward=home
Host: 192.168.254.254
Origin: http://192.168.254.254
Referer: http://192.168.254.254/index.html
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
X-Requested-With: XMLHttpRequest
"""

header_list = raw_headers.split('\n')
split_headers = []
for header in header_list:
    if len(header) > 1:
        split_headers.append(header.split(':'))

for idx, header in enumerate(split_headers):
    # print(header)
    # print(f'{idx+1} == {len(header_list)}')
    seperator = '' if (idx+1 == len(split_headers)) else ','
    print(f'\'{header[0].strip()}\': \'{header[1].strip()}\'{seperator}')