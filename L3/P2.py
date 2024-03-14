def cam_expos(a, b):
    f_number = ['f/1.4', 'f/2', 'f/2.8', 'f/4', 'f/5.6', 'f/8', 'f/11', 'f/16', 'f/22']
    shutter_speed = ['1/4', '1/8', '1/15', '1/30', '1/60', '1/125', '1/250', '1/500', '1/1000', '1/2000', '1/4000']
    ISO = ['100', '200', '400', '800', '1600', '3200']

    set_f = f_number.index(a[0]) - f_number.index(b[0])
    set_shutter = shutter_speed.index(a[1]) - shutter_speed.index(b[1])
    set_iso = ISO.index(b[2]) - ISO.index(a[2])
    overall = set_f + set_shutter + set_iso

    return set_f, set_shutter, set_iso, overall

if __name__ == '__main__':
    res = cam_expos(['f/2.8', '1/500', '400'], ['f/5.6', '1/125', '200'])
    print(res)