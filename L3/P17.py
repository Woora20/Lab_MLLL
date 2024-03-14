ratio = float(input("ratio: "))
sensitivity = float(input("sensitivity: "))
year = 0

while True:
    if ratio >= sensitivity:
        print("Year %d: ratio = %s"%(year, ratio))
        year += 5730
        ratio /= 2 
        if year == 0:
            pass
    elif sensitivity >= ratio:
        break


        
