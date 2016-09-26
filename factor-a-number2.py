import math
num = float(raw_input('What number would you like to factor? '))
for x in range(1, int(math.ceil(math.sqrt(num))) + 1):
    factors1 = ''
    factors2 = ''
    y = num / float(x)
    if y.is_integer() == True:
        factors1 += str(y)
        factors2 += str(float(x))
        print factors1, "and", factors2
