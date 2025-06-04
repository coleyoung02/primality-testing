import math, time

MAX_PRIME = 876417533

TARGET_MAX = 2 ** 30

def read_primes() -> tuple[set, list]:
    s = set()
    with open("primes.txt", "r") as new_p:
        for line in new_p:
            s |= {int(line.strip())}
    return s

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

def generate_primes(f, max_time):
    """
    runs prime algorithms for max_time seconds of cpu time.
    returns tuple with (largest prime generated, number of primes generated).
    """
    t = 0
    i = 2
    l = []
    while t < max_time * 1e9:
        start = time.process_time_ns()
        if (f(i, l)):
            end = time.process_time_ns()
            l.append(i)
        else:
            end = time.process_time_ns()
        i += 1
        t += end - start
    return (l[-1], len(l))

