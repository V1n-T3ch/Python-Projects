def is_prime(n):
    """Check if n is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
number = 2

while count < 1001:
    if is_prime(number):
        count += 1
    if count == 1001:
        print(number)
    number += 1