age = int(input("Input your age: "))

if (age < 13):
    print("You belong to \"Child\" group!")
elif (age < 20):
    print("You belong to \"Teenager\" group!")
elif (age < 60):
    print("You belong to \"Adult\" group!")
else:
    print("You belong to \"Senior\" group!")