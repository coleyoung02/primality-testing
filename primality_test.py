import math, time, random

from utils import *

MAX_PRIME = 876417533

TARGET_MAX = 2 ** 30

def get_prime_list() -> list:
    l = []
    with open("primes.txt", "r") as new_p:
        for line in new_p:
            l.append(int(line.strip()))
    return l


def naive(n, l=[]):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sqrt_n(n, l=[]):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def sqrt_n_list(n, list_so_far):
    stop_at = int(math.sqrt(n)) + 1
    for i in range(len(list_so_far)):
        if list_so_far[i] >= stop_at:
            break
        if n % list_so_far[i] == 0:
            return False
    return True

# true if likely prime
def mr_loop(n, b, k):
    temp = b
    for i in range(0, k):
        if pow(b, 2 ** i, n) == -1 % n:
            return True
        temp = pow(temp, 2, n)
    return False

# true if likely prime
def miller_rabin(n, a):
    """
    n is the number we test primality for, a is the intended witness
    """
    # n - 1 = (2 ** k) * q
    # b = a ** q (mod n)
    k = find_power_of_2_divisor(n - 1)
    q = int((n - 1) // (2 ** k))
    b = pow(a, q, n)
    return b == 1 or mr_loop(n, b, k)

def miller_randoms(n, k):
    for r in random.sample(range(2, n), k):
        if not miller_rabin(n, r):
            return False
    return True

def miller_random_plus_k_range(n, k):
    r = random.randint(2, n - k)
    for i in range(k):
        if not miller_rabin(n, r + i):
            return False
    return True

def miller_first_k(n, k):
    for i in range(2, k + 2):
        if not miller_rabin(n, i):
            return False
    return True



def test_miller_rabin():
    s = read_primes()
    for i in range(20, 2000000):
        if (miller_randoms(i, 3) != (i in s)):
            print("\t\tmr fail at", i, "randoms")
        if (miller_random_plus_k_range(i, 3) != (i in s)):
            print("\t\tmr fail at", i, "miller_random_plus_k_range")
        if (miller_first_k(i, 3) != (i in s)):
            print("\t\tmr fail at", i, "first_k")

if __name__ == "__main__":
    test_miller_rabin()