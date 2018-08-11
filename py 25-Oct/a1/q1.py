lengths = input('Enter side lengths: ')
# split by space
lengths = lengths.split()
# convert into integer
lengths = list(int(i) for i in lengths)
# equilateral
if lengths[0] == lengths[1] == lengths[2]:
    print('The triangle is an equilateral triangle.')
else:
    print('Sadly, the triangle is not equilateral. Find a better triangle.')
