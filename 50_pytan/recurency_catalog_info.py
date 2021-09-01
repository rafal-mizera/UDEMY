import os

def rec_catalog(dir):

    for el in os.listdir(dir):
        path = os.path.join(dir,el)
        if os.path.isdir(path):
            rec_catalog(path)
        else:
            print(path)
    return

print(rec_catalog("C:\\temp"))