height = int(raw_input('How tall? '))

for row_num in range(height):
    base_width = 2 * height - 1
    num_stars = (row_num * 2) + 1
    num_spaces = (base_width - num_stars) / 2
    spaces = " " * num_spaces
    stars = "*" *  num_stars
    print spaces + stars

# base_width = 2 * height - 1


# row 0 will always have 1 star

# If you cannot come up with a formula, list out a bunch of examples of what you need:

# 2 rows

# row 0: 1 space, 1 star
# row 1: 0 spaces, 3 stars

# 3 rows

# row 0: 2 spaces, 1 star
# row 1: 1 space, 3 stars
# row 2: 0 spaces, 5 stars

# 4 rows

# row 0: 3 spaces, 1 star
# row 1: 2 space, 3 stars
# row 2: 1 spaces, 5 stars
# row 3: 0 spaces, 7 stars





# print "   *"
# print "  ***"
# print " *****"
# print "*******"
