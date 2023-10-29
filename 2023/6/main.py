from collections import Counter
import sys
import math

def main():
    xy = [[], [], []]
    vtw = []
    for line in sys.stdin:
        temp = line.split(" ")
        if xy == [[], [], []]:
            i = 0
            while i < 6:
                xy[i//2] = [int(temp[i]), int(temp[i + 1])]
                i += 2
            print(xy)
        else:
            for item in temp:
                vtw.append(float(item))
            print(vtw)

            # start program

            # starting time
            t = 0
            currentPos = t * vtw[0]
            while (currentPos < vtw[2]):
                t += 1
                currentPos += vtw[0]
            #remove 1 from t since the loop stops after it is over
            t -= 1
            currentPos -= vtw[0]
            #check if any numbs are in q4 related to origin

            #rotation angle
            RA = float((360/t)/vtw[1])
            #update each point based on the current rotation angle
            for i in range(len(xy)):
                xy[i] = rotatePoint(xy[i], RA, currentPos)
            #check if rotation can reach

            print(findQuad(xy[0], t))
            # while currentPos < w
            #while (t * currentPos < vtw[2]):
                #print()

            #clear out per loop
            xy.clear()
            vtw.clear()

def findQuad(input, x):
    #check if number is in the right spot (y < 0 and x < x(input)
    if (input[0] < x and input[1] < 0):
        return True
    return False

def rotatePoint(inputPoint, RA, xOirigin):
    returnArr = [1, 1]
    #current angle
    CA = float(math.atan(float(inputPoint[0])/float(inputPoint[1])))
    #convert to degrees
    CA = CA * (180/math.pi)
    #fix angle
    angle = CA + RA
    if angle > 90 and angle < 181:
        returnArr[0] *= -1
    elif angle > 180 and angle < 270:
        returnArr[0] *= -1
        returnArr[1] *= -1
    else:
        returnArr[1] *= -1
    if abs(angle) > (90):
        angle = abs(abs(angle) - 180)
    #update x
    d1 = math.sqrt((xOirigin + inputPoint[0])**2+(inputPoint[1])**2)
    returnArr.append(returnArr[0] * (math.cos(math.radians(angle))) * d1)
    #update y
    d2 = math.sqrt((xOirigin + inputPoint[0])**2+(inputPoint[1])**2)
    returnArr.append(returnArr[1] * (math.sin(math.radians(angle))) * d2)

    return returnArr

main()