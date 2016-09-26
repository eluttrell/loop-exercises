num = int(raw_input('What multiplication table would you like to see? '))
for x in range(1, 11):
    sol = num * x
    print num, "x", x, "=", sol
