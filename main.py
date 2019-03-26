import math
while True == True:     #runs forever in a loop
    x1 = int(input('x1: '))   #input x1
    y1 = int(input('y1: '))   #input y1
    x2 = int(input('x2: '))   #input x2
    y2 = int(input('y2: '))   #input y2


    #slope intercept form (y=mx+b)
    SlopeY = y2-y1

    SlopeX = x2-x1
    Slope = SlopeY/SlopeX #calculates slope

    print('slope: ', Slope)   #prints out slope to user
    b = y1-(Slope*x1)   #calculates y intercept
    print("y-intercept: ",b)  #prints b
    print("equation:  y =","(",SlopeY,"/",SlopeX,")X+", b)   #prints the entire y = mx+b equation

    #mid point
    mid_x = x2-x1
    mid_y = y2-y1
    print('midpoint:  ',  '(' , mid_x, '/2,' , mid_y, '/2 )' )

    #distance
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    print('distance: ', distance)
