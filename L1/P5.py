import math

t = float(input('Impact duration (s): '))
m = float(input('Effective weight (kg): '))
r = float(input('Effective length (m): '))
T = float(input('Blow execution time (s): '))

# (1) Find angular velocity
w = 2 * math.pi / T
# (2) Find impact velocity
v = w * r
# (3) Find impact force
f = m * v / t

# (4) Convert units
kmh = v * 3600 / 1000
mph = kmh / 1.61
lbf = f / 4.45

velocity_report = "v = {:,.2f} km/h = {:,.2f} mph"
force_report = "f = {:,.2f} N = {:,.2f} lbf"

print(velocity_report.format(kmh, mph))
print(force_report.format(f, lbf))
