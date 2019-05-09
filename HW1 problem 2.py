# Homework problem #2
# setting up the funtion to check if the sequence of int values has a pair whose product is odd.
# I am assuming that, in the event a sinlge int is entered, it should return "False" since there is no
# pair with which to test with.
def isodd(nums): #main function to test if it is odd
    last = len(nums)
    x = 0
    while x < last:
        y = x + 1
        while y < last:
            if (nums[x] * nums[y]) % 2 != 0:
                return True
            y += 1
        x += 1
    return False


# calling the function
oddish = [] #variable that is tested
print('When finished entering values hit Ctrl+d')
while True:
    try:
        uinput = int(input('Enter an integer: '))
        oddish.append(uinput)
    except EOFError:
        break
print('It is', isodd(oddish), 'That there are values in ',oddish, ' that can produce an odd number when multiplied together')