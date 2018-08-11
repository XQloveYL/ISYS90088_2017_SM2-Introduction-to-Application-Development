expected = [str(i) for i in range(10)]+[' ']
# the digits 0-9 and the space character
integers = input('Enter integers: ')
integers_list = list(integers)
unexpected = False
for i in integers_list:
    # determine whether there is an unexpected character
    if i in expected:
        continue
    else:
        print('Error: invalid character ' "\"" + i + "\"")
        unexpected = True
        break
if not unexpected:
    integers = integers.split()
    if len(integers) == 0:
        # determine whether it is empty
        print('Sum: 0')
        print('Mean: 0.0')
        # the empty sum is equal to 0
    else:
        integers = [int(i) for i in integers]
        # convert into int and form a list
        print('Sum: '+str(sum(integers)))
        print('Mean: '+str(float(sum(integers)/len(integers))))
