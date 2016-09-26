height = int(raw_input("Height? "))
width = int(raw_input("Width? "))
for row_num in range(height):
    row = ''
    for col_num in range(width):
        if col_num == 0 or row_num == 0:
            row += '*'
        elif col_num == width - 1 or row_num == height - 1:
            row += '*'
        else:
            row += ' '
    print row
