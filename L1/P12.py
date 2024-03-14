import math
def tennis_service_another(ball_speed, court_length, ball_weight):
    time = 0
    Ej = 0
    Ecal = 0

    # (0) Convert speed and weight to SI units
    # v: speed in m/s
    v = ball_speed*5/18

    # m: mass in kg
    m = ball_weight/1000

    # distance d: in m

    # (1) compute the travel time t the ball takes;
    time = court_length*2/v

	#(2) compute an acceleration a, given initial speed (assuming 0) and final speed (assuming at top speed) and time t;
    a = v/time

	#(3) compute a force f required, then the energy E can be estimated.
    f = m*a
    Ej= f*0.5*a*time**2
    Ecal = Ej/4.184

    return time, Ej, Ecal

if __name__ == '__main__':
    print('Time = %.4f s. Energy = %.2f J = %.2f cal'%tennis_service_another(
        int(input('Enter the ball speed (km/h):')),
        float(input('Enter the court length (m):')),
        float(input('Enter the ball weight (g):'))))
    