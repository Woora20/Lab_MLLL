import math

def earthquake(events):
    result = []

    for event in events:
        date_location = event[0]
        magnitude = event[1]

        # Estimate energy using the given formula
        energy = 10**(4.8 + 1.5 * magnitude)

        result.append([date_location, magnitude, energy])

    return result

if __name__ == "__main__":
    events = [['2019 02 22 Ecuador', 7.5],
              ['2018 08 19 Fiji', 8.2],
              ['2017 09 08 Mexico', 9.1]]

    res = earthquake(events)
    print(res)
