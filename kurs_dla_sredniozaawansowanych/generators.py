ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = ((start, stop) for start in ports for stop in ports if start < stop)

# for x in routes:
#     try:
#         print(next(routes))
#     except StopIteration:
#         print("All items were viewed")

counter = 0
for (start, stop) in routes:
    print("{} - {}".format(start, stop))
    counter += 1

print(counter)
