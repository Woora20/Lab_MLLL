def calculate_force(distance, spring_constant):
    return spring_constant * distance

x = float(input("Enter distance (m): "))
k = float(input("Enter spring constant (N/m): "))

force = calculate_force(x, k)
print("The force is {} N".format(force))
