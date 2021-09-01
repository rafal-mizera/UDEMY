ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connections = []
for port1 in ports:
    for port2 in ports:
        if port1 != port2 and port1 < port2:
            connections.append((port1,port2))


print(connections,len(connections))
