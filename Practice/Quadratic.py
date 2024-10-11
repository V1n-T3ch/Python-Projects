a = int(input("Enter Coefficient a: "))
b =int(input("Enter Coefficient b: "))
c = int(input("Enter Coefficient c: "))
b2 = b*-1

srt = b**2 + (4*a*c) 

if srt > 0:
    x1 = (b2+(srt)**0.5)/(2*a)
    x2 = (b2-(srt)**0.5)/(2*a)
    print(f"Root1 is: {x1}")
    print(f"Root2 is: {x2}")
elif srt == 0:
    x = b2 / (2*a)
    print(f"Root is: {x}")
else:
    print("This is a Complex Root")