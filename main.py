try:
    from sympy.mpmath import mp
except ImportError:
    from mpmath import mp

def indexPi(number):
    for i in range(10**(len(number)+5)):
        mp.dps = i
        if(str(mp.pi).replace(".","")[-len(number)-1:-1] == number):
            return(i - len(number))
    return("Out of range")

def PiEncode(Snumber,depth):
    lengthList = []
    for i in range(depth):
        lengthList.append(len(Snumber))
        Snumber = indexPi(Snumber)
    return(Snumber,lengthList)


number = input("input the number to be indexed:\n")

position = indexPi(number)

print("your number is located {}".format(position))

print("checking result")

mp.dps = position + len(number)
print(str(mp.pi)[-len(number)-1:-1])
