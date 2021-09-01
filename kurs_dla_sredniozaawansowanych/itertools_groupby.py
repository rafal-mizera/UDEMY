import os, itertools

def scantree(path):
    for el in os.scandir(path):
        if el.is_dir():
            yield el
            yield from scantree(el.path)
        if not el.is_dir():
            yield el


listing = scantree(r"C:\\Users\RMZ\PycharmProjects")
listing = sorted(listing,key= lambda x: x.is_dir())

for el in listing:
    if el.is_dir():
        print(f"{el} jest folderem plików")
    if not el.is_dir():
        print(f"{el} jest plikiem")

for is_dir, elements in itertools.groupby(listing,key=lambda e: e.is_dir()):
    print(print('DIR ' if is_dir else 'FILE', len(list(elements))))