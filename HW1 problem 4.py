#Homework Problem #4
# setting up the class
class HAM:
    def __init__(self,p1,p2):#constructor
        self.x = p1
        self.y = p2
        # This variable measures the hamming distance
        self.ham_time = 0
        # Now to determine which value is the largest.
        self.big = max(x,y)
        self.sml = min(x,y)
    #This method converts integers into their binary equivilent
    def tobin(self,b):
        bina = []
        while b != 0:
            bina.insert(0, b % 2)
            b = b // 2
        return bina
    #this method will add the needed 0's to the smaller list
    def addZero(self,b,s):
        q = len(b) - len(s)
        while q > 0:
            s.insert(0, 0)
            q -= 1
        return s
    #Finally, it is time to find the hamming distance with this method
    def countHam(self):
        bigbin = self.tobin(self.big)
        smlbin = self.tobin(self.sml)
        if len(bigbin) != len(smlbin): #Need to add 0s to small to make comparison easier
            smlbin = self.addZero(bigbin,smlbin)
        q = 0
        while q < len(bigbin):
            if bigbin[q] != smlbin[q]:
                self.ham_time += 1
            q += 1
        return self.ham_time
x = int(input('Enter X for Hamming distance: '))
print()
y = int(input('Enter Y for Hamming distance: '))
print()
#Need to test that the x and y values are within parameters
while x < 0:
    print('X must be >= 0')
    x = int(input('Enter X: '))

while y >= pow(2,31):
    print('Y must be less than 2^31')
    y = int(input('Enter Y: '))

h = HAM(x,y)
print('Hamming distance is : ',h.countHam())