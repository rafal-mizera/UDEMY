channels = {"Google": 1480, "Email": 300, "Natural Traffic": 440, "TV Spot": 700}
print(channels["Email"])
channelsUpdate = {"Natural Traffic": 520,"News": 600}
channels.update(channelsUpdate)
print(channels.keys())
channels.pop("Email")