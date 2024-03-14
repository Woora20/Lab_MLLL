def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def approx_sin(x, M, tolerance=1e-10, max_iterations=1000):
    sinv = 0
    for i in range(M):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / fact(2 * i + 1)
        sinv += term

        # Check for convergence
        if abs(term) < tolerance:
            break

        # Check for maximum iterations
        if i == max_iterations - 1:
            print("Warning: Maximum iterations reached without convergence.")

    return sinv

if __name__ == '__main__':
    x = float(input('x:'))
    M = int(input('M:'))

    result = approx_sin(x, M)
    print('sin(%.2f) = %.5f' % (x, result))
