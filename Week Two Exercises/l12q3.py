import numpy as np
m = np.array([[0,1,2,3,4,5],
           [10,11,12,13,14,15],
           [20,21,22,23,24,25],
           [30,31,32,33,34,35],
           [40,41,42,43,44,45],
           [50,51,52,53,54,55]])

def blue(nparray):
    output_list = []
    for x in nparray:
        for y in x:
            if y%10 == 1:
                output_list.append(int(y))
    return output_list

def pink(nparray):
    output_list = []
    x1 = 1
    for x1 in nparray:
        for y in x1:
            if y == 12 or y == 13:
                output_list.append(int(y))
            if 12 in output_list and 13 in output_list:
                break
    return output_list

def green(nparray):
    output_list = []
    for x1 in nparray[2:4]:
        for y in x1:
            if y%10 == 5 or y%10 == 4:
                output_list.append(int(y))
    return output_list

def orange(nparray):
    output_list = []
    for x in nparray[2:5]:
        for y in range(0, len(x), 2):
                output_list.append(int(y))
    return output_list


print(m[0:,1:2])
print(m[2::2, 0::2])
print(m[1:2, 2:4])
print(m[2:4, 4:])

# b = blue(m)
# print(b)
# p = pink(m)
# print(p)
# g = green(m)
# print(g)
# o = orange(m)
# print(o)


#import tensorflow
#print(tensorflow.version.VERSION)

