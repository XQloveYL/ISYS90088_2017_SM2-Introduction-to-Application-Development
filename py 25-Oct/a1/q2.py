num = input('Enter the number: ')
# keep the digit, filter other symbol
num = filter(str.isdigit, num)
# convert into int and form a list
num = [int(i) for i in num]
print('The number contains ' + str(len(num)) + ' digits')
print('The digits sum to ' + str(sum(num)))
