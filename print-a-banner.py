banner = raw_input('What would you like your banner to display?\n:')
caps = raw_input('Would you like it in all caps? y for yes, n for no. \nIf you select no the text will display exactly as you type it.')
for row_num in range(3):
    row = ''
    star_num = len(banner) + 4
    if row_num == 0 or row_num == 2:
        row += '*' * star_num
    elif row_num == 1:
        row += "* %s *" % banner
    if caps == 'y':
        print row.upper()
    else:
        print row
