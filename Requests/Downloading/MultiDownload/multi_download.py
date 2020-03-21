import time
from os import stat, path
import requests
import tqdm
import concurrent.futures


def is_resumable(url):
    headers = requests.head(url).headers
    return "accept-ranges" in headers, headers['content-length']


def download(url):
    headers = {}
    write_type = "wb"

    # create filename from url
    url_list = url.split('/')
    file_name = url_list[len(url_list) - 1]

    # check if file already exists
    if path.exists(file_name):
        file_size = stat(file_name).st_size
        resumable = is_resumable(url)
        # check if file has already been downloaded
        if file_size == int(resumable[1]):
            # dont download
            print(f"Already downloaded...")
            return True, url
        elif resumable[0]:
            # resume if possible
            headers = {'range': f'bytes={file_size}'}
            write_type = "ab"
            print(f"Resuming Download From: {file_size}")
        else:
            # download from start
            print(f"Unable To Resume...Re-Downloading...")

    resp = requests.get(url, headers=headers)
    if resp.ok:
        with open(file_name, write_type) as f:
            for chunk in resp.iter_content(chunk_size=1024):
                f.write(chunk)
            return True, url
    else:
        return False, url


if __name__ == "__main__":
    pass
    start = time.perf_counter()

    download_list = []
    with open("files.txt", "r") as f:
        lines = f.read().split("\n")
        for line in lines:
            download_list.append(line)

    # download_list = [_ for _ in range(21)]
    dl_per_set = 1

    dl_split = f"{len(download_list)/dl_per_set}".split('.')

    additional_iter = 1 if int(dl_split[1]) > 0 else 0
    download_iterations = int(dl_split[0]) + additional_iter
    downloads_left = len(download_list)
    dlstart = 0
    dlend = dl_per_set

    print(f"Total Downloads: {len(download_list)}")
    print(f"Download Per Set: {dl_per_set}")
    print(f"Download Sets: {download_iterations}\n")

    for iteration in range(download_iterations):
        print("="*25)
        print(f"Download Set({iteration+1})")
        print(f"Downloading {download_list[dlstart:dlend]}")

        with concurrent.futures.ThreadPoolExecutor() as ex:
            results = ex.map(download, download_list[dlstart:dlend])
            for result in results:
                print(result)
        if iteration + 1 == download_iterations:
            downloads_left -= downloads_left
            print('Last Iteration')
        else:
            dlstart += dl_per_set
            dlend += dl_per_set
            downloads_left -= dl_per_set
        print(f'Downloads Left: {downloads_left}')
        print("=" * 25)
        print("\n")

    end = time.perf_counter()

    print(f"Finished in {end-start}(s)")





