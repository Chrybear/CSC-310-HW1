# Homework Problem #1
wordbank = []
while True:
    try:
        print('When finished press Ctrl+d')
        uinput = input('Enter word(s):')
        wordbank.append(uinput)
    except EOFError:
        break

print()#For spacing
#Now we print out all those values in reverse
last = len(wordbank)-1
while last >= 0:
    print(wordbank[last])
    last-=1