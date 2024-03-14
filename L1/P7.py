angle = float(input("Angle (degree): "))
distance = float(input("Distance (km): "))

# Calculate circumference using Eratosthenes' method
earth_circumference = 360 * distance / angle

report = 'Eratosthenes: "the earth circumference is about {:,.1f} km."'
print(report.format(earth_circumference))

