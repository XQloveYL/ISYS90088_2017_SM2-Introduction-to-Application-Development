price = float(input('Enter purchase price ($): '))

# Header:
columns = ['Month', 'Opening Bal', 'Interest',
           'Principal', 'Repayment', 'Closing Bal']
header = ''
for i in columns:
    header += '| {} '.format(i)
# delete the first '|'
header = header[1:]
print('-' * len(header))
print(header)
print('-' * len(header))

# Content:
downpay = 12/100 * price
# 17-month repayment plan
for i in range(1,18):
    mthrepay = 6/100 * price
    # The monthly repayment must be at least $0.01
    if mthrepay < 0.01:
        break
    # down payment at the beginning
    if i == 1:
        openbalance = price - downpay
    else:
        openbalance = closebalance
    # round to 2 decimal places
    interest = round(openbalance * 0.15 / 12, 2)
    if openbalance < mthrepay:
        mthrepay = openbalance + interest
    principal = mthrepay - interest
    closebalance = round(openbalance + interest - mthrepay, 2)
    line = ''
    line += '| {:<{}} '.format(i, len(columns[0]))
    # show 2 decimal places
    line += '| {:<{}.2f} '.format(openbalance, len(columns[1]))
    line += '| {:<{}.2f} '.format(interest, len(columns[2]))
    line += '| {:<{}.2f} '.format(principal, len(columns[3]))
    line += '| {:<{}.2f} '.format(mthrepay, len(columns[4]))
    line += '| {:<{}.2f} '.format(closebalance, len(columns[5]))
    line = line[1:]
    # print row one by one
    print(line)
