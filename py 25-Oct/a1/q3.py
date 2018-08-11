string = input('Enter string: ')
# set a bool to help to determine whether the for loop have returned something
repeat = False
# substring cannot be the entire string, only go through the first half
for i in range(len(string)//2):
    # only consider factor
    if len(string) % (i + 1) == 0:
        # go through every substring with the length = len(i)
        sub = string[0:i+1]
        # determine whether the string is exactly composed by substring
        if string.count(sub) * sub == string:
            print("Congratulations, " +
                  "\"" + string + "\"" + " is made up of " +
                  str(string.count(sub)) + " repetitions of " +
                  "\"" + sub + "\"")
            # if condition satisfied, change the value of "re"
            repeat = True
            break
if not repeat:
    print("Bummer, " +
          "\"" + string + "\"" +
          " is not made up of repetitions of a substring")
