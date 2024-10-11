num = int(input("Enter a Number: "))
power = len(str(num))

sum = 0
temp = num

while temp > 0:
    dig = temp % 10
    sum += dig ** power
    temp //= 10

if sum == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not an Armstrong Number")