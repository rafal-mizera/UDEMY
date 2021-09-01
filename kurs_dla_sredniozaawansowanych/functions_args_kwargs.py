def calculatePaint(efficency_ltr_per_m2,*args):
    needed_paint = efficency_ltr_per_m2 * sum(args)
    return  print("You need",needed_paint, "litres of paint")

print(calculatePaint(0.25, 42, 28, 30))

rooms = [10,20,30]
calculatePaint(2,*rooms)

#########################################################################
import os

def logIt(*args):
    with open(r"c:\temp\log_it.txt", "a") as f:
        for arg in args:
            f.write(arg)
            f.write(" ")
        f.write("\n")


logIt('Starting processing forecasting')
text = ["Report", "is", "being", "prepared"]
logIt(*text)
