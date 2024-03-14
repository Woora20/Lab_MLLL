import math

def Hipparchus(do, theta_m):
    # Compute distance to the moon
    Dm = do / (2 * math.tan(math.radians(theta_m)))

    # Compute the range if the measure is off by 0.01 degree
    Dml = do / (2 * math.tan(math.radians(theta_m + 0.01)))
    Dmu = do / (2 * math.tan(math.radians(theta_m - 0.01)))

    # Sort the range in ascending order
    Dml, Dmu = sorted([Dml, Dmu])

    return Dm, Dml, Dmu

def Aristarchus(dm, theta_s):
    # Compute distance to the sun
    Ds = dm / math.tan(math.radians(theta_s))

    # Compute the range if the measure is off by 0.01 degree
    Dsl = dm / math.tan(math.radians(theta_s + 0.01))
    Dsu = dm / math.tan(math.radians(theta_s - 0.01))

    # Sort the range in ascending order
    Dsl, Dsu = sorted([Dsl, Dsu])

    return Ds, Dsl, Dsu

if __name__ == '__main__':
    res_h = Hipparchus(400, 89.97)
    print('Hipparchus: {:.2f} km; [{:.0f}, {:.0f}] if 0.01 deg off'.format(*res_h))

    res_a = Aristarchus(381972, 0.15)
    print('Aristarchus: {:.2f} km; [{:.0f}, {:.0f}] if 0.01 deg off'.format(*res_a))
