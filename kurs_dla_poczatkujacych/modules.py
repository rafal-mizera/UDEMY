percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,

           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,

           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,

           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,

           8.740978348,6.174819567]

percent = sorted(percent)


from statistics import median_high,median,median_low

print(median(percent))
print(median_low(percent),median_high(percent))
#####################################################################################
import math


# 1° = (π * rad) / 180
# 1 rad = 180° / π

degree = 360
degree2 = 45
radian = 180 / math.pi
print(radian)

print("360 degree =",round(degree/radian,2),"radians")
print("45 degree =",round(degree2/radian,2),"radians")

print(math.radians(360))
print(math.radians(45))

###########################################################################
small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38
small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22

small_pizza_area = math.pi * small_pizza_r**2
big_pizza_area = math.pi * big_pizza_r**2
family_pizza_area = math.pi * family_pizza_r**2
print(small_pizza_area,big_pizza_area,family_pizza_area)

areas = [small_pizza_area,big_pizza_area,family_pizza_area]
prices = [small_pizza_price,big_pizza_price,family_pizza_price]

print(small_pizza_price/small_pizza_area,"zł za m2")

for x,y in zip(areas,prices):
    print(y/x,"zł za m2")

######################################################
math_ls = dir(math)
print(math_ls)
