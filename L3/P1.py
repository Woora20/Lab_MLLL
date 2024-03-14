import math

def cos_sim(a, b):
    s_d1 = 0
    s_d2 = 0
    s_up = 0

    for i in range(0, len(a)):
        s_up += a[i] * b[i]
        s_d1 += a[i] ** 2
        s_d2 += b[i] ** 2

    s = s_up / (math.sqrt(s_d1) * (math.sqrt(s_d2)))

    return s

if __name__ == '__main__':
    cs2 = cos_sim([14, 0, 5], [5, 8, 4])
    print(cs2)
