height = int(raw_input("Height? "))
width = int(raw_input("Width? "))
print "*" * width
for cube in range(height - 2):
    print "*" + " " * (width - 2) + "*"
print "*" * width
