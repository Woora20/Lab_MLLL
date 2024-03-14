import math

def calc_energy_another(mass, final_speed, time_interval):
    E = 0
    d = 0

    acc = (final_speed - 0) / time_interval
    force = mass * acc
    d = 0 + (0.5 * acc * time_interval ** 2)
    E = force * d

    return E, d

if __name__ == '__main__':

    g = lambda f: f(float(input('object mass:')),
                    float(input('target speed:')),
                    float(input('time spent:')))
    print("Energy = %.2f J. Distance = %.2f m."%g(calc_energy_another))
