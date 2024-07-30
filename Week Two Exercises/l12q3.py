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

a = blue(m)
print(a)

