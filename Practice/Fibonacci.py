terms = int(input("Enter number of Terms to Generate: "))

term1, term2 = 0, 1
count = 0

if terms <= 0:
    print("Enter a Positive Integer")
elif terms == 1:
    print("Fibonacci Sequence up to {0}st:".format(terms))
    print(term1)
else:
    print("Fibonacci Sequence up to {0}th:".format(terms))
    while count < terms:
        print(term1)
        nth = term1 + term2
        term1 = term2
        term2 = nth
        count +=1
    
        