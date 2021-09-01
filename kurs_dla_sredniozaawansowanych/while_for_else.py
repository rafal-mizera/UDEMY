import os, urllib.request

data_dir = r"C:\\temp"
pages = [{ 'name': 'Flashscore',      'url': 'http://www.flashscore.com/'},

    { 'name': 'Wikipedia', 'url': 'http://wikipedia.org/' },

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'}]

for page_adr in pages:
    try:
        file_name = f"{page_adr['name']}.html"
        path = os.path.join(data_dir,file_name)
        print("Saving page in catalog...", path)
        urllib.request.urlretrieve(page_adr["url"],path)
        print("Done!")
    except:
        print('FAILURE processing web page: {}'.format(page["name"]))
        print('Stopping the process!')
        break
else:
    print("All pages downloaded succesfully!")

