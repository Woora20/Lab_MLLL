pm25 = float(input("PM2.5: "))

if 12 >= pm25 >= 0:
    print("AQI: Good")
elif 35.5 > pm25 > 12:
    print("AQI: Moderate")
elif 55.5 > pm25 >= 35.5 :
    print("AQI: Unhealthy for Sensitive Groups")
elif 150.5 > pm25 >= 55.5:
    print("AQI: Unhealthy")
elif 250.5 > pm25 >= 150.5:
    print("AQI: Very Unhealthy")
elif 350.5 > pm25 >= 250.5:
    print("AQI: Hazardous")
elif 500 >= pm25 >= 350.5:
    print("AQI: Hazardous")
else:
    print("Invalid PM2.5 level. Please enter a valid value.")