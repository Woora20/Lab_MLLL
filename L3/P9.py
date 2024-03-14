def sweet(fsweet, fdrink):
    # Retrieve sweetness dict
    sweetness = {}
    sweetness_d = {}

    # Read sweetness information from 'sweetness1.txt'
    with open(fsweet, "r") as d:
        next(d)  # Skip header
        for line in d:
            sub, swtness, cal = line.split()
            sweetness[sub] = float(swtness)

    # Read drink information from 'CocaPanda.txt'
    with open(fdrink, 'r+') as fs:
        for line in fs:
            sub_d, swtness_d = line.split()
            sweetness_d[sub_d] = float(swtness_d)

    # Calculate the estimated sweetness
    sweet_sum = sum(sweetness.get(sub_d, 0) * swtness_d for sub_d, swtness_d in sweetness_d.items())

    # Write/append message to the end of the file
    msg = "\nSweet as {:.1f}% sucrose solution".format(sweet_sum)

    with open(fdrink, "a+") as coca:
        coca.write(msg)

if __name__ == '__main__':
    sweet('sweetness1.txt', 'CocaPanda.txt')
