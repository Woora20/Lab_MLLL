# Get input from the user
fuel_density = float(input("Fuel density (in kg/L): "))
calorific_value = float(input("Calorific value (in MJ/kg): "))

# Calculate energy per volume
energy_per_volume_mjL = fuel_density * calorific_value
energy_per_volume_bbl = energy_per_volume_mjL * 158.987

# Display the results
print("This fuel has energy per volume of %.2f MJ/L." % energy_per_volume_mjL)
print("That is %.2f MJ/bbl." % energy_per_volume_bbl)
