age = int(input("Enter your age: "))
day = "Wednesday"

ticketPrice1 = 8.00
ticketPrice2 = 12.00

if(age < 18):
    print("Child")
    if(day == "Wednesday"):
        ticketPrice1 = ticketPrice1 - 2.00
    print("Movie ticket price is", ticketPrice1, "Dollars")
else:
    print('Adult')
    if(day == "Wednesday"):
        ticketPrice2 = ticketPrice2 - 2.00
    print("Movie ticket price is", ticketPrice2, "Dollars")