import time
import requests
from os import stat, path
import json

from tqdm import tqdm

if __name__ == "__main__":
    download_url = "https://cdn1.mangafox.online/554/113/962/488/25/soredemo-ayumu-wa-yosetekuru.jpg"
    raw_split = download_url.split('/')
    file_name = raw_split[len(raw_split)-1]

    headers = requests.head(download_url).headers
    content_length = headers['content-length']

    request_headers = {}
    write_type = "wb"
    downloaded = 0

    if "accept-ranges" in headers and path.exists(file_name):
        # resume download from last position
        downloaded = stat(file_name).st_size
        request_headers = {'range': f'bytes={downloaded}-{content_length}'}
        print(f'Resuming Download: {downloaded}-{content_length}')
        write_type = "ab"

    if downloaded == int(content_length):
        print(f"File has been downloaded.\n-> {file_name}")
    else:
        resp = requests.get(download_url, headers=request_headers, stream=True)
        print(resp.request.headers)
        with open('headers.txt', 'w+') as f:
            f.write(str(resp.headers))

        with open(file_name, write_type) as f:
            with tqdm(total=int(content_length)) as pbar:
                for chunk in resp.iter_content(chunk_size=1024):
                    pbar.update(len(chunk))
                    downloaded += len(chunk)
                    f.write(chunk)

