import time, math

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

def generate_probable_primes(f, k, max_time):
    """
    runs miller-rabin with max k passes for max_time seconds of cpu time.
    returns tuple with (largest prime generated, number of primes generated).
    """
    t = 0
    i = 2
    l = []
    while t < max_time * 1e9:
        start = time.process_time_ns()
        if (f(i, k)):
            end = time.process_time_ns()
            l.append(i)
        else:
            end = time.process_time_ns()
        i += 1
        t += end - start
    return (l[-1], len(l))

def generate_miller_verfied(miller, verify, k, max_time):
    t = 0
    i = 2
    l = []
    while t < max_time * 1e9:
        start = time.process_time_ns()
        if (miller(i, k) and verify(i, [])):
            end = time.process_time_ns()
            l.append(i)
        else:
            end = time.process_time_ns()
        i += 1
        t += end - start
    return (l[-1], len(l))



def find_power_of_2_divisor(n):
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


# testing if squaring previous values or squaring individually performs better
def compare():
    m = 19231201818401
    k = 1241
    b = 98212447
    temp = 0
    start1 = time.process_time_ns()
    for i in range(k):
        temp = pow(b, 2 ** i, m)
    print(time.process_time_ns() - start1)
    last = b
    start2 = time.process_time_ns()
    for i in range(k):
        last = pow(last, 2, m)
    print(time.process_time_ns() - start2)

def read_primes(filepath="large_files/new_primes.txt") -> tuple[set, list]:
    s = set()
    with open(filepath, "r") as new_p:
        for line in new_p:
            s |= {int(line.strip())}
    return s

if __name__ == "__main__":
    compare()


