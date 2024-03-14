def simple_poet(p):
    with open(p, "r") as f:
        lines = f.read().splitlines()

    return lines

if __name__ == '__main__':
    res = simple_poet('poem.txt')
    print(res)
