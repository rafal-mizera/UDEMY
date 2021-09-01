q = "THE EYES"
print(q[0] + q[1] + q[2] + q[5] + q[3] + q[7] + q[4] + q[6])

q = "a gentleman"
print(q[3]+q[6]+q[7]+q[2]+q[0]+q[4]+q[5]+q[1]+q[8]+q[9:])

line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[line.find(":")+2:]
print(time)

tmp = line[line.find('"')+1:]
print(tmp)
title = tmp[:tmp.find('"')]
print(title)