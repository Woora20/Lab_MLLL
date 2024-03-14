def typhoon(wspeed, adensity, area, height):
    storm_scale = [['Category 5', 252],
                   ['Category 4', 209],
                   ['Category 3', 178],
                   ['Category 2', 155],
                   ['Category 1', 119],
                   ['Tropical Storm', 63],
                   ['Tropical Depression', 0]]

    # Find storm type
    storm = None
    for category, threshold in storm_scale:
        if wspeed >= threshold:
            storm = category
            break

    # wind velocity in m/s
    v = wspeed / 3.6

    # air density in Kg/cu. m
    rho = adensity

    # Area in sq. m
    A = area * 1e6

    # Height in m
    H = height

    # air mass in Kg
    m = rho * A * H

    E = 0.5 * m * v**2

    return [storm, E]

if __name__ == '__main__':
    results = []

    for v in range(0, 280, 10):
        res = typhoon(v, 1.225, 80424, 15240)
        results.append(res)
        # rho = 1.225 kg/cu. m
        # A = diameter 160 km ~ 80424 sq km
        # H = 50000 ft = 15240m
        print('%d km/h:'%v, '{} Energy {:,.5} J'.format(res[0], res[1]))
