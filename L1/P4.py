import math

if __name__ == '__main__':
    v = float(input('Plane speed (mph):'))
    T = float(input('Interval between crash and the last contact (h):'))
    
    Area = math.pi*(v*T)**2
    report = "Search area = {:,.2f} sq.mi."
    print(report.format(Area))
    
    Thailand = 198120
    Area_Perspective = Area/Thailand
    perspective = "That's {:,.2f} time(s) the size of Thailand."
    print(perspective.format(Area_Perspective))


    