# largest of 3 numbers
a = 25
b = 35
c = 45
if a > b and a > c:
    print("a is the largest number")
if b > a and b > c:
    print("b is the largest number")
if c > a and c> b:
    print("c is the largest number")
#########################################################
yesterday_volume = 3500000
today_volume = 459990

if today_volume > yesterday_volume:
    print("Go Long")
if today_volume < yesterday_volume:
    print("Go short")
#########################################################
open_price_today = 13500
if open_price_today > 13500:
    print("Go Long")
else:
    print("Go Short")



