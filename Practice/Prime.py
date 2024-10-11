num = int(input("Enter a Number: "))

if num == 1:
    print("{0} is not a Prime Number".format(num))
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break
        else:
            flag = False

if flag:
    print("{0} is not a Prime Number".format(num))
else:
    print("{0} is a Prime Number".format(num))