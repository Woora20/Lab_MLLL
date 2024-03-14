R = int(input('R Channel[0-255]:'))
G = int(input('G Channel[0-255]:'))
B = int(input('B Channel[0-255]:'))
# Fill in your code.

Y = 0.2126*R+0.7152*G+0.0722*B

# Do not edit below this line
# ---------------------------------

print("Y = %d" % (Y))