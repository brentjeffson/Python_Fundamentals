import requests
from datetime import datetime
import time
import xml.dom.minidom as xml
import json


URL = 'http://192.168.8.1/'
STATUS_API = 'api/monitoring/status'
TRAFFIC_API = 'api/monitoring/traffic-statistics'
SESSION_ID = 'd3roljPTGZmVu1pfF00ckSXih4JZNjxtM6eDhvCFhHPB6XtTju33Bifi0TN1imX1TZ6Kf1YaqHt3x1D3JgSgGTVIZPeRA8XmPXsR0BMy00Tk0rJrqvDxw0pJZIQ0aANb'

if __name__ == '__main__':
    s = requests.Session()
    s.headers.update({})
    s.cookies.update({'SessionID': SESSION_ID})

    while True:
        resp = s.get(URL + TRAFFIC_API)
        
        if resp.ok:
            
            doc = xml.parseString(resp.text)

            total_upload = int(doc.getElementsByTagName('TotalUpload')[0].firstChild.nodeValue)
            total_download = int(doc.getElementsByTagName('TotalDownload')[0].firstChild.nodeValue)

            print(datetime.now().strftime('%I:%M:%S%p'))
            if len(str(total_download)) >= 7:
                ttotal_download = total_download/1024/1024
                ttotal_upload = total_upload/1024/1024
                print(f'Total Upload: {ttotal_upload:.2f}MB\nTotal Download: {ttotal_download:.2f}MB')
            elif len(str(total_download)) >= 4: 
                ttotal_download = total_download/1024
                ttotal_upload = total_upload/1024
                print(f'Total Upload: {ttotal_upload:.2f}KB\nTotal Download: {ttotal_download:.2f}KB')
            else:
                print(f'Total Upload: {total_upload} byte\nTotal Download: {total_download} byte')
            
            with open('traffic_stat.log', 'at+') as f:
                f.write(f"{datetime.now()}:{total_upload}:{total_download}\n")
        else:
            print("Please Change Session ID")
            SESSION_ID = input()
            continue
        print('*'*64)
        time.sleep(60)


