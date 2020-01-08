class Chapter:
    title = ''

    def __init__(self, title):
        self.title = title


chapters = [
    Chapter('All Hail The King'),
    Chapter('All Kings Die'),
    Chapter('Return Of The Lord'),
]

old_chapter = chapters[1]
print('Before Replacement')
for chapter in chapters:
    print(chapter.title)

new_chapter = Chapter('The New Chapter Begins')
index_to_replace = chapters.index(old_chapter)
chapters[index_to_replace] = new_chapter
print('\n\nAfter Replacement')
for chapter in chapters:
    print(chapter.title)







