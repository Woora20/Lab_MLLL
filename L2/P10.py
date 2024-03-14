def sailor_mate(wind, boat):
    wind = ((int(wind.split(":")[0]) - 1) * 30) + (int(wind.split(":")[1]) * 0.5)
    boat = ((int(boat.split(":")[0]) - 1) * 30) + (int(boat.split(":")[1]) * 0.5)

    result = abs(wind - boat)
    new_head_dir = boat - wind 

    if result == 0:
        return "run"

    direction = "starboard" if new_head_dir > 0 else "port"

    if 0 < result <= 45 or 45 < result < 90:
        return "{} broad reach".format(direction)
    elif result == 90:
        return "{} beam reach".format(direction)
    elif result < 135:
        return "{} close hauled".format(direction)
    else:
        return "tacking"

# Testing the function with the provided code
if __name__ == "__main__":
    r = sailor_mate("9:00", "12:00")
    print("9:00", "12:00", r)

    ticks = [
        "12:00",
        "1:30",
        "1:31",
        "2:59",
        "3:00",
        "3:01",
        "5:59",
        "6:00",
        "6:01",
        "8:59",
        "9:00",
        "9:01",
        "10:29",
        "10:30",
    ]

    for b in ticks:
        r = sailor_mate("6:00", b)
        print("6:00", b, r)
