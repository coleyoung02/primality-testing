import math, time

MAX_PRIME = 15485863

def read_primes() -> set:
    s = set()
    with open("primes.txt", "r") as new_p:
        for line in new_p:
            s |= {int(line.strip())}
    return s


def naive(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sqrt_n(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    start = time.process_time_ns()
    last = start
    primes = read_primes()
    for i in range(2, MAX_PRIME):
        if (i % 1000) == 0:
            print(i, time.process_time_ns() - last)
            last = time.process_time_ns()
        if sqrt_n(i) != (i in primes):
            print("wrong", i)