def star_lagtime(light_speed, name, distance):
    t = (distance * 1000) / light_speed
    print(name)
    return t

if __name__ == '__main__':
    t = star_lagtime(299792458, "sun", 149.6e6)
    print(t)
    print("{:,.2f} s = {:,.2f} min.".format(t, t/60))