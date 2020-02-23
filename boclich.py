print("2020")
d = int(input("Enter solar calendar day: "))
m = input("Enter solar calendar month: ")
if m == "January":
    if (d>=1) and (d<=24):
        a = d+6
        ma = 12
        print(f"Lunar date is {a}, lunar month is {ma}")
        print("Year 2019")
    elif (d==25):
        a = d -24
        ma = 1
        print(f"Lunar date is {a}, lunar month is {ma}")
        print("Happy New Year 2020")
    elif (d>25) and (d<=30):
        a = d -24
        ma = 1
        print(f"Lunar date is {a}, lunar month is {ma}")
    else:
        print("Dumb")
elif m == "February":
    if (d>=1) and (d<=22):
        a = d+7
        ma == 1
        print(f"Lunar date is {a}, lunar month is {ma}")
    elif (d>=23) and (d<=29):
        a = d -22
        ma = 2
        print(f"Lunar date is {a}, lunar month is {ma}")
    else:
        print("Dumb")
elif m == "March":
    if (d>=1) and (d<=23):
        a = d+7
        ma =2
        print(f"Lunar date is {a}, lunar month is {ma}")
    elif (d>=24) and (d<=31):
        a = d -23
        ma = 3
        print(f"Lunar date is {a}, lunar month is {ma}")
    else:
        print("Dumb")
elif m =="April":
    if (d>=1) and (d<=22):
        a = d+8
        ma = 3
        print(f"Lunar date is {a}, lunar month is {ma}")
    elif (d>=23) and (d<=30):
        a = d -22
        ma = 4
        print(f"Lunar date is {a}, lunar month is {ma}")
    else:
        print("Dumb")
elif m =="May":
    if (d>=1) and (d<=22):
        a = d +8
        ma = 4
        print(f"Lunar date is {a}, lunar month is {ma}")
    elif(d>=23) and (d<=31):
        a = d - 22
        ma = 4
        print(f"Lunar date is {a}, lunar month is {ma}")
    else:
        print("Dumb")
elif m == "June":
    if (d>=1) and (d<=20):
        a = d + 9
        ma = 4
        print(f"Lunar date is {a}, lunar month is {ma}")
    elif(d>=21) and (d<=30):
        a = d - 20
        ma = 5
        print(f"Lunar date is {a}, lunar month is {ma}")
    else:
        print("Dumb")
elif m == "July":
    if (d>=1) and (d<=20):
        a = d+10
        ma = 5
        print(f"Lunar date is {a}, lunar month is {ma}")
    elif (d>=21) and (d<=31):
        a = d -20
        ma = 6
        print(f"Lunar date is {a}, lunar month is {ma}")
    else:
        print("Dumb")
elif m == "August":
    if (d>=1) and (d <=18):
        a = d+11
        ma = 6
        print(f"Lunar date is {a}, lunar month is {ma}")
    elif(d>=19) and (d<=31):
        a = d - 18
        ma = 7
        print(f"Lunar date is {a}, lunar month is {ma}")
    else:
        print("Dumb")
elif m == "September":
    if (d>=1) and (d<=16):
        a = d+13
        ma = 7
        print(f"Lunar date is {a}, lunar month is {ma}")
    elif (d>=17) and (d<=30):
        a = d -16
        ma = 8
        print(f"Lunar date is {a}, lunar month is {ma}")
    else:
        print("Dumb")
elif m == "October":
    if (d>=1) and (d<=16):
        a = d + 14
        ma = 8
        print(f"Lunar date is {a}, lunar month is {ma}")
    elif (d>=17) and (d<=31):
        a = d - 16
        ma = 9
        print(f"Lunar date is {a}, lunar month is {ma}")
    else:
        print("Dumb")
elif m =="November":
    if (d>=1) and (d<=14):
        a = d + 15
        ma = 9
        print(f"Lunar date is {a}, lunar month is {ma}")
    elif (d>=15) and (d<=30):
        a = d - 14
        ma = 10
        print(f"Lunar date is {a}, lunar month is {ma}")
    else:
        print("Dumb")
elif m =="December":
    if (d>=1) and (d<=13):
        a = d + 16
        ma = 10
        print(f"Lunar date is {a}, lunar month is {ma}")
    elif (d>=14) and (d<=31):
        a = d -13
        ma = 11
        print(f"Lunar date is {a}, lunar month is {ma}")
    else:
        print("Dumb")
else:
    print("I have nothing to show you")

