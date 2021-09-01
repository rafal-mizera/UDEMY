import requests
import os
import shutil
import urllib3.exceptions


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = 'c:/temp/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
    print(f"Removing {tmpfile}......")
    save_url_to_file(url,tmpfile_path)

    print('Copying file {} {}'.format(tmpfile_path, file_path))
    shutil.copy(tmpfile_path, file_path)

except requests.exceptions.ConnectionError as e:
    print(f"Failed to download from {url}")
    print(f"Error details: {e}")

except PermissionError as e:
    print(f"{tmpfile_path} is a file available only for read")
    print(f"Details: {e}")

except FileNotFoundError as e:
    print(f"Cannot find file. Please check the path: {tmpfile}")
    print(f"Details: {e}")

except Exception as e:
    print("Error...")
    print(f"Details : {e}")

else:
    print("Download completed succesfully!")

finally:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
    print("File deleted....")



