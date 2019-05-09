# Homework Problem #3

#helper method
def permu(num):
    perm(num,0,len(num)-1)
#function to swap
def swap(num, x, y):
    tmp = num[x]
    num[x] = num[y]
    num[y] = tmp
    return num
#main recursive function
def perm(num, x, y):
    if x == y:
        print(num)
    else:
        m = x
        while m <= y:
            num = swap(num,x,m)
            perm(num,x+1,y)
            #The main list is changing every swap, so we need to ensure it resets back to the original state
            num = swap(num,x,m)
            m+=1
print('Enter values to find their permutations. When finished enter Ctrl+d')
perlist = []
while True:
    try:
        uinput = int(input('Enter a number: '))
        perlist.append(uinput)
    except EOFError:
        break
permu(perlist)