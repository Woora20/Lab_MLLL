def mighty_river(rivers):
    river_power = {}

    for river, values in rivers.items():
        A, rho, Q = values
        power = 0.5 * (1 / A**2) * rho * Q**3
        river_power[river] = power

    return river_power

if __name__ == '__main__':
    mighties = {'Amazon': [1.2e6, 1100, 210000],
                'Congo': [2e6, 1150, 41200],
                'Yangtze': [800e3, 1200, 30000]}

    river_power = mighty_river(mighties)
    print(river_power)
