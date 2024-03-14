import math

def brunelleschi_lamp(vx, vy, x, y, height, d, logfile='log.txt'):
    # Calculate the angle and length between two points
    L, beta = find_pol(vx, vy, x, y)

    # Deduce H and tau
    H = (L - d) * math.sin(beta)
    tau = (L - d) * math.cos(beta)

    # Calculate the angle pointing from top of the reference post toward the vanishing point
    theta = math.pi - find_pol(vx, vy, x, y + height)[1]

    # Deduce h'
    phi = math.pi - theta
    hprime = H - tau * math.tan(phi)

    # Write input and calculation details to the log file
    inp_msg = "Input: vx={:.2f}, vy={:.2f}, x={:.2f}, y={:.2f}, height={:.2f}, d={:.2f}.\n"
    inp_msg = inp_msg.format(vx, vy, x, y, height, d)

    calc_msg = "Calc: L = {:.2f}, beta = {:.2f}, H = {:.2f}, tau = {:.2f}, phi = {:.2f}, h' = {:.2f}.\n"
    calc_msg = calc_msg.format(L, beta, H, tau, phi, hprime)

    with open(logfile, 'a') as f:
        f.write(inp_msg)
        f.write(calc_msg)

    return hprime

def find_pol(vx, vy, x, y):
    # Calculate the angle and length between two points
    dx = vx - x
    dy = vy - y
    L = math.sqrt(dx**2 + dy**2)
    beta = math.atan2(dy, dx)

    return L, beta

if __name__ == '__main__':
    # Example 1
    vx, vy = 0, 75
    x, y = 100, -100
    height = 40
    d = 0
    res = brunelleschi_lamp(vx, vy, x, y, height, d)
    print('Ans =', res)

    # Example 2
    from mama_turtle import road
    r = road()
    r.draw_road()
    r.draw_lamp_posts(brunelleschi_lamp)
    input('enter to exit')
