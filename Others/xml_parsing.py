import xml.dom.minidom as xml


doc = xml.parse("response.xml")
print(doc.nodeName)
print(doc.firstChild.tagName)

total_upload = doc.getElementsByTagName('TotalUpload')[0]
total_download = doc.getElementsByTagName('TotalDownload')[0]
print(total_upload.firstChild.nodeValue)
print(total_download.firstChild.nodeValue)
