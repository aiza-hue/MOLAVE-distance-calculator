import math
# ask users to input the coordinates 

x1 = float(input("Enter x-coordinate of point 1:" ))
y1 = float(input("Enter y-coordinate of point 1:" ))
x2 = float(input("Enter x-coordinate of point 2:" ))
y2 = float(input("Enter x-coordinate of point 2:" ))

# compute the distance using the distance formula
distance = math.sqrt(math.pow(x2 - x1, 2) + (math.pow(y2 - y1, 2)))

# display the result rounded by two decimal places
print ("The distance betwen the two points is", distance)

#using the library makes it much easier to code and takes less time to code. sqrt and pow were the easiest to use, because if those function werent there, the coding will take longer

