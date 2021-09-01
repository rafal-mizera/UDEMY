import os,functools
import datetime as dt
import requests

def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            file = open(log_file_path, "a")
            file.write(f"{logged_action} on file: {path} {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            result = func(path)
            return result
        return the_real_wrapper
    return wrapper_with_log_to_known_file


@wrapper_with_log_file("FILE_CREATE",r"c:/temp/file_create.txt")
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")

@wrapper_with_log_file("DELETE_FILE",r"c:/temp/delete_file.txt")
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r"C:/temp/zadanie_wrappery")
delete_file(r"C:/temp/zadanie_wrappery")

########################################################################################################
def wrapper_log_to_file(url,file_path):
    def logger(func):
        def wrapper():
            file = open(file_path,"a")
            file.write(f"Downloaded data from: {url}\n")
            file.write(30*"-")
            result = func()
            return result
        return wrapper
    return logger







@wrapper_log_to_file("http://api.nbp.pl/api/exchangerates/tables/C/",r"C:/temp/log_exchange.txt")
def exchange_downloader():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C/")
    json_response = response.json()
    file = open(r"C:/temp/exchange.txt","a")
    for dict in json_response:
        for el in dict.items():
            el = str(el)
            file.write(el)
    return

exchange_downloader()



