#declaring the weather daytime list variable
weather_list_day = []
#opening the weather data day text file
with open("weather_data_day.txt") as f:
    #giving the weather list day variable a job to search for intergers
    weather_list_day = [int(item) for item in f.readlines()]

#calculating the min, max, and average of the daytime tempatures through out the week
minimum = min(weather_list_day)
maximum = max(weather_list_day)
average = sum(weather_list_day)/len(weather_list_day)

#declaring the weather nighttime list variable
weather_list_night = []
#opening the weather data day text file
with open("weather_data_night.txt") as fp:
    #giving the weather list day variable a job to search for intergers
    weather_list_night = [int(item) for item in fp.readlines()]

#calculating the min, max, and average of the daytime tempatures through out the week
minimum1 = min(weather_list_night)
maximum1 = max(weather_list_night)
average1 = sum(weather_list_night)/len(weather_list_night)

#printing the results of the script
print("The highest day-time temperature is, " + maximum)
print ("The lowest day-time tempature is, " + minimum)
print("The average day-time tempature is, " + average)
print("The highest night-time tempature is, " + maximum1)
print("The lowest night-time tempature is, " + minimum1)
print("The average night-time tempature is, " + average1)