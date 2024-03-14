"""
Student's Name: !!!Write your name here!!!
ID: !!!Write your id here!!!
Diatonic notes on scale.
Print all diatonic notes on scale, given the scale key.
"""

from P8_helper import print_scale # Keep this untouched

# Make the diatonic function work

def diatonic(scale_key):
    # Fix this to work on all keys
    # Hint: recall the triad exercise question
    n1 = scale_key
    n2 = (n1 + 2) % 12
    n3 = (n1 + 4) % 12
    n4 = (n1 + 5) % 12
    n5 = (n1 + 7) % 12
    n6 = (n1 + 9) % 12
    n7 = (n1 + 11) % 12

    return n1, n2, n3, n4, n5, n6, n7

if __name__ == "__main__":

    key_of = int(input('Enter the key [1-12]:'))
    k1, k2, k3, k4, k5, k6, k7 = diatonic(key_of)
    print_scale(k1, k2, k3, k4, k5, k6, k7)
    if key_of == 7:
        s = __doc__
        sname = s.split('P20')[0]
        print(sname)

