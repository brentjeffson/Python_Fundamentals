
class Download:
    URL = "url"
    RESUMABLE = "resumable"
    FILENAME = "filename"
    RAWBYTES = "rawbytes"
    DIRECTORY = "directory"
    CONTENT_LENGTH = "filesize"
    
    def __init__(self, url, directory=".", content_length=-1, resumable=False, filename=None):
        self._url = url
        self._directory = directory
        self._resumable = resumable
        self._filename = filename
        self._content_length = content_length
    
    def get(self, cancel_download=None, headers={}, params={}, chunk_size=1024):
        try: 
            download = Download._get(self, cancel_download=cancel_download, headers={}, params={}, chunk_size=1024)
        except FileDownloadedException as e:
            downloads = Download.load(path)
            if self.url in downloads:
                Download._remove(self.url, path)
            return self
        else:
            return download
            
        
    def save(self, path):
        if Path(self.filename).exists() and self.filesize == self.content_length and self.url in Download.load(path):
            Download._remove(self.url, path)
            return
        elif self.resumable:
            Download._save(self, path)
        
                
    @staticmethod
    def load(path):
        if not Path(path).exists():
            Path(path).touch()
            return {}
        if os.stat(path).st_size <= 0:
            return {}
        with open(path, "rt") as f:  
            downloads = json.loads(f.read())
        return downloads
    
    @staticmethod
    def parse_filename(url):
        extensions = ["co", "org", "us", "com", "gov", "corp", "net", "int", 
                      "mil", "edu", "gov", "ru", "biz", "info", "jobs", "mobi",
                      "name", "ly", "tel", "kitchen", "email", "tech", "state",
                      "xyz", "codes", "bargains", "bid", "expert", "io"
                     ]
        while url[-1] == "/":
            url = url[:-1]
        filename = url.split("/")[len(url.split("/"))-1]
        ext = filename.split(".")[len(filename.split("."))-1]
        if ext in extensions:
            filename += ".html"
        
        return filename        
                
    @staticmethod
    def _remove(url_to_remove, path):
        downloads = Download.load(path)
        downloads.pop(url_to_remove)
        
        if len(downloads) == 0:
            Download._clear(path)
            return downloads
        
        for url in downloads:
            download = downloads[url]
            Download._save(
                Download(url, download[Download.DIRECTORY], download[Download.CONTENT_LENGTH], download[Download.RESUMABLE]),
                path
            )
        
        return downloads
    
    @staticmethod
    def _clear(path):
        try: 
            with open(path, "wt+") as f:
                f.write("")
            return True
        except:
            return False
    
    @staticmethod
    def _get(download, cancel_download=None, headers={}, params={}, chunk_size=1024):
        global CANCEL
        tstart = time.time()
        mode = "ab"

        if Path(download.filename).exists():
            print(f"File Found: `{download.filename}`")
            
            if download.content_length == -1:
                resp = requests.get(download.url, headers=headers, params=params)     
        
                if not resp.ok:
                    return None
                
                content_length = int(resp.headers["content-length"]) if "content-length" in resp.headers else -1
                resumable =  True if "accept-ranges" in resp.headers else False
                
                if download.filesize >= content_length:
                    print(f"File Already Downloaded -> lsize:{download.filesize} - rsize:{content_length}")
                    raise FileDownloadedException(f"File Already Downloaded -> lsize:{download.filesize} - rsize:{content_length}")
            
            print(f"Resuming Download: {download.filesize}-{content_length}")
            headers.update({"range": f"bytes={download.filesize}-{content_length}"})
        
        resp = requests.get(download.url, headers=headers, params=params)     
        if resp.ok:
            if "range" not in resp.request.headers:
                content_length = int(resp.headers["content-length"]) if "content-length" in resp.headers else -1
            resumable =  True if "accept-ranges" in resp.headers else False
            print(f"Downloading: {download.filename} -> lsize:{download.filesize if Path(download.filename).exists() else 0} - rsize:{content_length}")
            
            with open(download.filename, mode) as f:
                size_downloaded = 0
                for chunk in resp.iter_content(chunk_size=chunk_size):
                    
#                     if cancel_download is not None:
#                         if cancel_download():
                    if CANCEL:
                        print(f"Cancelling Download: Downloaded {size_downloaded}/{content_length}:{(size_downloaded/content_length)*100}%")
                        return Download(url=download.url, directory=download.directory, content_length=content_length, resumable=resumable)
                            
                    
                    f.write(chunk)
                    size_downloaded += len(chunk)
       
        
        tend = time.time()
        print(f"Succesfully Downloaded: {download.filename}:{(size_downloaded/content_length)*100}%")
        print(f"Download Time: {tend-tstart}s")
        return Download(url=download.url, directory=download.directory, content_length=content_length, resumable=resumable)
    
    @staticmethod
    def _save(download, path):
        downloads = Download.load(path)
        downloads.update({download.url: {
                Download.DIRECTORY: download.directory, 
                Download.RESUMABLE: download.resumable,
                Download.FILENAME: download.filename,
                Download.CONTENT_LENGTH: download.content_length
            }
        })
        with open(path, "wt") as f:
            f.write(json.dumps(downloads, indent=4))
        print(f"Download Info Saved: {download.url} Saved To File {path}")
    
    @property
    def url(self):
        return self._url
    
    @property
    def directory(self):
        return self._directory
    
    @property
    def resumable(self):
        return self._resumable
    
    @property
    def filename(self):
        if self._filename != None:
            return self._filename
        return self.parse_filename(self.url)
    
    @property
    def filesize(self):
        return Path(self.filename).stat().st_size
    
    @property
    def content_length(self):
        return self._content_length