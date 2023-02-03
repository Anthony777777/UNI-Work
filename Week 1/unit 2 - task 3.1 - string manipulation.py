
# total string
weather = "Friday\nTomorrow, variable cloud will tend to clear through the morning, with plenty of winter sunshine developing. However, patchy cloud and isolated showers may move in from the west later in the afternoon."

#split on )
print(weather.split())
#split on \n
print(weather.split("\n"))
#split on ,
print(weather.split(","))
#split on .
print(weather.split("."))

#find total length of weather
print(len(weather))

#convert to lower case
weather_lc = weather.lower()
print(weather_lc)

#find the position of sunshine as part of the index
print(weather.find("sunshine"))

# confiming sunshine is in the string the != is python for is not eqaul to
if weather.find("sunshine") != -1:
    print("it will sunshine")
else:
    print ("no sunshine")

# replacing the . with a paragraph mark, the way below keeps the full stop and adds a paragraph mark as well
new_weather_string = weather.replace(". ", ".\n")
print(new_weather_string)