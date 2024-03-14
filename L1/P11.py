import math

def find_num_bits(num_states):

    num_bits = math.ceil(math.log2(num_states))
    return num_bits

if __name__ == '__main__':
    g_another = lambda f: f(int(input('Enter # possible states:')))
    print(g_another(find_num_bits))



