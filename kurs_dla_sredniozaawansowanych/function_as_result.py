from datetime import datetime
def functionCreator(type):

    if type == "m":
        sec = 60
    elif type == "h":
        sec = 3600
    elif type == "d":
        sec = 86400


    source = """
def f(date_1,date_2):
    result = date_2 - date_1
    result_in_s = result.total_seconds()
    return divmod(result_in_s, {})[0]""".format(sec)

    exec(source, globals())

    return f

start = datetime(2019, 1, 1, 0, 0, 0)
end  = datetime.now()
f_minutes = functionCreator('m')
f_hours = functionCreator('h')
f_days = functionCreator('d')

print(f_days(start,end))
print(f_minutes(start,end))
