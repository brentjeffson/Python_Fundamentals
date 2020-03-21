import time
import threading
import concurrent.futures


urls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_active_downloads = 0

def get_url(url):
    time.sleep(1)
    return url

with concurrent.futures.ThreadPoolExecutor(2) as executor:       
    results = [executor.submit(get_url, url) for url in urls]
    # results = []
    # while len(urls) > 0:
    #     print(f"Start Retrieval For {urls[0]}")
    #     results.append(executor.submit(get_url, urls[0])) 
    #     print(f"Removing Url {urls[0]}")
    #     urls.remove(urls[0])
    
    for f in concurrent.futures.as_completed(results):
        print(f.result())
        print(threading.currentThread().name)
    
    




