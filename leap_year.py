year = 2000

if (year % 4 == 0):
    if ((year % 100 != 0) or (year % 400)) == 0:
        print("Leap Year!")
    else:
        print("Not Leap Year!")
else:
    print("Not Leap Year!")