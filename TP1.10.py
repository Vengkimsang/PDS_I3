def is_prime(n):
    if n < 2:
        return False
    # Test divisors up to the square root of n for speed
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def goldbach(n):
    # Every even number >= 4 is the sum of two primes
    # We test prime values of p starting from 2 up to n // 2
    p = 2
    while p <= n // 2:
        if is_prime(p) and is_prime(n - p):
            return (p, n - p)
        p += 1
    return None

# 1. Print all primes below 50 on one line
primes_below_50 = [str(n) for n in range(2, 50) if is_prime(n)]
print("Primes below 50:", " ".join(primes_below_50))

# 2. Count primes below 100
primes_below_100_count = sum(1 for n in range(2, 100) if is_prime(n))
print(f"Number of primes below 100: {primes_below_100_count}")

# 3. Print Goldbach pairs for even numbers from 4 to 30
for n in range(4, 32, 2):
    p, q = goldbach(n)
    print(f"{n} = {p} + {q}")

# 4. Check Goldbach's conjecture for every even number from 4 to 10,000 using break
conjecture_holds = True
for n in range(4, 10001, 2):
    if goldbach(n) is None:
        conjecture_holds = False
        break

print(f"Goldbach holds for every even number from 4 to 10000: {conjecture_holds}")