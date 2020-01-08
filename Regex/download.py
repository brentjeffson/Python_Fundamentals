import requests

if __name__ == '__main__':
    r = requests.get('https://mangakakalot.com/chapter/rx919523/chapter_71')
    if r.ok:
        with open('manga_item_content.html', 'w+', encoding='utf-8') as f:
            f.write(r.text)










