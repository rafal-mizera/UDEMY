helloMessage = "Hello %s!"
print(helloMessage %"Kate")
print(helloMessage %"Chris")

helloMessage1 = "Hello {0:s}!"
print(helloMessage1.format("Kate"))
print(helloMessage1.format("Chris"))

message = "%s has %d %s"
print(message % ("Kate",1,"animal"))
print(message % ("Chris",1000,"$"))

message2 = "{0:s} has {1:d} {2:s}"
print(message2.format("Kate",1,"animal"))
print(message2.format("Chris",100,"$"))

line = "%20s costs %6d €"
print(line %("ICE CREAM",3))
print(line %("TRIP TO VENICE",119))
print(line %("PIZZA HAWAII",6))