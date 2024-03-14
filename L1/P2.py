def convert_rice_quantity(kwian):
    tang = kwian * 100
    kilogram = tang * 10
    return tang, kilogram

kwian = int(input("Enter rice quantity (kwian): "))
tang, kilogram = convert_rice_quantity(kwian)

output_format = "{} kw = {} tg = {} kg"
print(output_format.format(kwian, tang, kilogram))
