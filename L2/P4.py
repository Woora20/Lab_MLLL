def martian_botanist(number_of_plants, daily_growth_rate, production_rate):
    # Calculate total plants over time
    total_plants = number_of_plants * daily_growth_rate

    # Calculate planting area based on production rate
    planting_area = total_plants / production_rate

    return planting_area


if __name__ == "__main__":
    area = martian_botanist(150, 2, 2.4)
    print('planting area:', area, 'sq. m.')

    area = martian_botanist(900, 2.5, 1.2)
    print('planting area:', area, 'sq. m.')

    area = martian_botanist(200, 2.4, 1.6)
    print('planting area:', area, 'sq. m.')
