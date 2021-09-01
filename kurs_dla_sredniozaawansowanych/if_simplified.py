price = 123
bonus = 23
bonus_granted = False
#
# if bonus_granted:
#     price -= bonus
#
# print(price)


price_updated = price if not bonus_granted else price - bonus

print(price_updated)

##################################################################

rating = 3

# if rating == 5:
#     print('very good')
# elif rating == 4:
#     print('good')
# else:
#     print('weak')

print("very good" if rating == 5 else "good" if rating == 4 else "weak")

#####################################################################
import datetime

today_weakday = datetime.datetime.today().weekday() + 2
print(today_weakday)

print("pomagam mamie" if today_weakday == 0 else "Ty masz w domu pranie" if today_weakday == 1 or today_weakday == 2 else "Ja mam dyżur" if today_weakday == 3 else "Mam dwa zebrania" if today_weakday == 4 else "Ty nie możesz" if today_weakday == 5 else "NIEDZIELA BĘDZIE DLA NAS!!!")