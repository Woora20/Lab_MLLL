def calculate_rain_water(area_size, rain_density, raining_hours):
    rainfall = rain_density * raining_hours
    total_water = rainfall * (area_size * 1600)
    return total_water

if __name__ == '__main__':
    area_name = input('Area name:')
    print('{}: rain water = {:,.2f} L'.format(area_name, calculate_rain_water(
        float(input('Size of the area (in rai):')),
        float(input('The area rain density (in mm/h):')),
        float(input('The number of raining hours:'))
    )))

