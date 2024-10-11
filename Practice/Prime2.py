start = 1
stop = 10

print("Prime numbers between", start, "and", stop, "are:")

for num in range(start, stop + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)