num = float(raw_input('What number would you like to factor? '))
for x in range(1, int(num) + 1):
    factors = ''
    y = num / float(x)
    if y.is_integer() == True:
        factors += str(y)
        print factors
