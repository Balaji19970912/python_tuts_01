weather_type = "Cloudy"

if weather_type == "Sunny":
    activity = "Go for a walk!"
    # print("Go for a walk!")
elif weather_type == "Rainy":
    activity = "Read a book!"
    # print("Read a book!")
elif weather_type == "Snowy":
    activity = "Build a snowman!"
    # print("Build a snowman!")
else:
    activity = "Netflix and chill guru!"
    # print("Netflix and chill guru!")
print("Today's weather is \"",weather_type,"\" and you can",activity)