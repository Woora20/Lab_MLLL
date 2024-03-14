import math

CD = float(input('CD: '))
CL = float(input('CL: '))
rho = float(input('air density: '))
A = float(input('cross-section area: '))
S = float(input('wing area: '))
m = float(input('plane weight: '))

# (1) find v from lift = weight: CL (0.5 rho v^2) S = m g;
g = 9.8  # m/s^2
v = math.sqrt(m * g / (S * CL * 0.5 * rho))

# (2) find drag: drag = CD (0.5 rho v^2) A;
drag = CD * (0.5 * rho * (v**2)) * A

# (3) find thrust: thrust = drag;
thrust = drag

# (4) find power: power = thrust * v.
power = thrust * v

# Convert power to horsepower
hp = power * 0.00136

report = "power = {:,.2f} W. = {:,.2f} hp."
print(report.format(power, hp))
