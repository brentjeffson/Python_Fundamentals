import re


def clean(src, str_list):
    for str in str_list:
        src = src.replace(str, '')
    return src

# search all manga chapter
with open('manga_item.html', encoding='utf-8') as f:
    doc = f.read()

    pattern = re.compile(r'<div id="chapter".+<div class="comment-info">', re.DOTALL)
    res = re.search(pattern, doc)

    start = int(res.span()[0])
    end = int(res.span()[1])
    doc = doc[start:end]

    res = re.findall(r'<a href.+</a>', doc)

    links = []
    for item in res:
        pattern = re.compile(r'href="(.+)"\s')
        res = re.search(pattern, item)
        print(res.groups()[0])
        print(res.group())
        if res is not None:
            pos = res.span()
            item = item[pos[0]:pos[1]]
            item = clean(item, ['href="', '"'])
            links.append(item)
            # links.append(item[pos[0]:pos[1]].replace('href="', '').replace('"',''))

    for link in links:
        print(link)











