
import tensorflow
print(tensorflow.version.VERSION)
path = "/Users/jadencheung/Documents/GitHub/ROAR-Academy/Week Two Exercises"

try:

    fil = open(path +'/' + 'motto.txt', 'w')
    fil.write("Fiat Lux\n")
finally:
    fil.close

try:
    with open(path + '/' + 'motto.txt', 'a') as fil:
        fil.write("Let there be light!\n")
finally:
    fil.close


