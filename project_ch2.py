import math
def tavan(x,y):
    return x**y

def baghi(x,y):
    return x%y

def menha(x,y):
    return x-y

def taghsim(x,y):
    return x/y  

def tol_ragham(x):
    return len(x)

def sins(x):
    return math.sin(x)

def tann(x):
    return math.tan(x)

def logg(x):
    return math.log10(x)

def coss(x):
    return math.cos(x)

def binn(x):
    return bin(x)

def hexxa(x):
    return hex(x)


print("\n", "MASHIN HESAB")

cou = 1
while cou != 0:
    print("""

        Select from the list below , then insert:
        ________________________
        1)  +     | 2)   -
        __________|_____________
        3)   *    | 4)   /     
        __________|_____________
        5) power  | 6) mod
        __________|_____________
        7 - sin   | 8 - tan
        __________|_____________
        9 - cos   | 10 - log10
        __________|_____________
        11 - number lenght
        ________________________
        12 - binary code
        ________________________
        13 - hexadecimal code
        ________________________
        """)

    x=0
    xj = 0
    yj = 0
    xm = 0
    ym = 0
    m=0
    tt=0
    xz = 1
    yz = 0
    xt = 0
    yt = 0
    yp=0
    yb=0
    index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11, 13]
    jam=list()
    men=list()
    zar=list()
    tag=list()
    khoroj=""
    vorodi = int(input(" What number do you want?   "))

    while vorodi not in index:
        print("THAST WRRONG DO IT AGAIN :)")
        vorodi = int(input(" What number do you want?   "))

    if vorodi == 1:
        t = int(input("Number of input digits   "))
        for i in range(1, t+1):
            print("digit %i  :     " %(i))
            yj = float(input())
            jam.append(yj)
        for ii in range(0,len(jam)):
            xj=xj+jam[ii]
        print(xj)
        t=0
        i=0
        ii=0
    elif vorodi == 2:
        while khoroj.upper != "e":
            xm=float(input("digit 1:      "))
            ym=float(input("digit 2:     "))
            print(menha(xm,ym))
            khoroj=input("exit :  e |||| continue :  any key ------->  ") 
            print("\n")
    elif vorodi == 3:
        t = int(input(" Number of input digits  "))
        for i in range(1, t+1):
            print("digit %i  :     " %(i))
            yz = float(input())
            zar.append(yz)
        for ii in range(0,len(zar)):
            xz=xz*zar[ii]
        print(xz)
        t=0
        i=0
        ii=0
    elif vorodi == 4:
        while khoroj != "e":
            xt=float(input("digit 1:      "))
            yt=float(input("digit 2:     "))
            print(taghsim(xt,yt))
            khoroj=input("exit :  e |||| continue :  any key ------->  ")
            print("\n")
    elif vorodi == 5:
        x = float(input(" digit   :     "))
        yp = float(input(" digit   :     "))
        print("\n", tavan(x,yp), "\n")
    elif vorodi == 6 :
        x = float(input(" digit   :     "))
        yb = float(input(" digit   :     "))
        print("\n", baghi(x,yb), "\n")
    elif vorodi == 11 :
        x = input("digit   :     ")
        print("\n", tol_ragham(x), "\n")
    elif vorodi == 7:
        x = float(input(" digit   :     "))
        print("\n", sins(x), "\n")
    elif vorodi == 8:
        x = float(input(" digit  :     "))
        print("\n", tann(x), "\n")
    elif vorodi == 9:
        x = float(input(" digit   :     "))
        print("\n", coss(x), "\n")
    elif vorodi == 10:
        x = float(input(" digit   :     "))
        print("\n", logg(x), "\n")       
    elif vorodi == 12:
        x = int(input(" digit   :     "))
        print("\n",binn(x), "\n")
    elif vorodi == 13:
        x = int(input(" digit   :     "))
        print("\n",hexxa(x), "\n")

    cou = int(input("continue : 1 ||||| exit: 0 --------->>   "))
    print("\n")
    while cou > 1:
        print("THAST WRRONG DO IT AGAIN ")
        cou = int(input("continue : 1 ||||| exit: 0 --------->>   "))
        print("\n")

print("GOOD LUCK")