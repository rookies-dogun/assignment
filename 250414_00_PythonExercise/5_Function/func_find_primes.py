


    
    
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(start, end):
    if(start < 2 or end < 2 or start > end):
        return "제대로 된 값이 아닙니다."
    
    return [num for num in range(start, end + 1) if is_prime(num)]

print(find_primes(2, 10))

    