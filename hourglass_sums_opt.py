# This is a simplified version - hourglass_sums.py shows each step of the loop to better visualize what's going on. 

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    v = 1
    for _ in range(6):
        print("Row", v, ": Enter 6 numbers each separated by a space")
        v += 1
        arr.append(list(map(int, input().rstrip().split())))


print("")
# Prints the array
for n in range(6):
    print(arr[n])

hourglass = []

# function assigns a - g to corresponding hourglass positions in the 6 x 6 array, finds the sum for the hourglass and if it's the max it's saved as the hourglass_max variable. This iterates for each 
# possible hourglass combination at the array using [0][0] as the origin. I'd like to mess around with the (x, y) because I think there's probably a way to do this so that you can run the function without 
# having to set (0, 0) as the starting argument every time. 
def HourglassSum(x, y):
    hourglass_sum = 0
    hourglass_max = 0
    for x in range(4):
        for y in range(4):
            a = arr[x][y]
            b = arr[x][y + 1]
            c = arr[x][y + 2]

            d = arr[x + 1][y + 1]

            e = arr[x + 2][y]
            f = arr[x + 2][y + 1]
            g = arr[x + 2][y + 2]

            hourglass.extend([a, b, c, d, e, f, g])
            hourglass_sum = a + b + c + d + e + f + g
            if hourglass_sum > hourglass_max:
                hourglass_max = hourglass_sum
            hourglass.clear()

    print("")
    print("The largest Hourglass Sum is: ", hourglass_max)
    return hourglass_max


HourglassSum(0, 0)
