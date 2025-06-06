from primality_test import *
from utils import generate_primes, read_primes
import const
import sys

output_directory = "test_outputs"
str_to_func = {"random": miller_randoms, "random_k_range": miller_random_plus_k_range, "first_k": miller_first_k}
size_to_bounds = {"small": (const.SMALL_LOW, const.SMALL_HI),
                  "med": (const.MED_LOW, const.MED_HI),
                  "large": (const.LARGE_LOW, const.LARGE_HI)}
size_to_filepath = {"small": const.SMALL_FILEPATH,
                    "med": const.MED_FILEPATH,
                    "large": const.LARGE_FILEPATH}


def prime_generation_tests():
    with open(f"{output_directory}/generated_up_to.csv", "+w") as up_to:
        with open(f"{output_directory}/generated_n_primes.csv", "+w") as n_primes:
            up_to.write("seconds,max int from naive,max int from sqrt n, max int from sqrt n with prime list\n")
            n_primes.write("seconds,primes from naive,primes from sqrt n, primes from sqrt n with prime list\n")
            for i in [1, 2, 5, 10, 30, 60, 120, 300]:
                nai = generate_primes(naive, i)
                sqt = generate_primes(sqrt_n, i)
                sql = generate_primes(sqrt_n_list, i)
                up_to.write(f"{i},{nai[0]},{sqt[0]},{sql[0]}\n")
                n_primes.write(f"{i},{nai[1]},{sqt[1]},{sql[1]}\n")
                print(f"Finished with {i} seconds per run")
                up_to.flush()
                n_primes.flush()

def miller_accuracy(miller_test_type: str, size:str):
    low = size_to_bounds[size][0]
    hi = size_to_bounds[size][1]
    test = str_to_func[miller_test_type]
    
    primes = read_primes(size_to_filepath[size])

    with open(f"{output_directory}/miller_{miller_test_type}_{size}.csv", "+w") as test_out:
        test_out.write("n,k=1,k=2,k=3\n")
        for i in range(low, hi):
            if (i % ((hi - low) // 10)) == 0:
                print("finished", i)
            line = f"{i},"
            for k in range(1, 4):
                line += str(int(test(i, k) == (i in primes))) + ","
            test_out.write(line[:-1] + "\n")
            
def miller_speed(miller_test_type: str):
    with open(f"{output_directory}/generated_up_to_miller.csv", "+w") as up_to:
        with open(f"{output_directory}/generated_n_primes_miller.csv", "+w") as n_primes:
            up_to.write("seconds,max int from k=1,max int from k=2, max int from k=3\n")
            n_primes.write("seconds,primes from k=1,primes from k=2, primes from k=3\n")
            for i in [1, 2, 5, 10, 30, 60, 120, 300]:
                k1 = generate_probable_primes(str_to_func[miller_test_type], 1, i)
                k2 = generate_probable_primes(str_to_func[miller_test_type], 2, i)
                k3 = generate_probable_primes(str_to_func[miller_test_type], 3, i)
                up_to.write(f"{i},{k1[0]},{k2[0]},{k3[0]}\n")
                n_primes.write(f"{i},{k1[1]},{k2[1]},{k3[1]}\n")
                print(f"Finished with {i} seconds per run")
                up_to.flush()
                n_primes.flush()


def large_primes_speed_test():
    miller_clock = 0.0
    sqrt_clock = 0.0
    interval_size = 50000
    powers_of_10 = [5, 6, 7, 8]
    with open(f"{output_directory}/large_prime_speed_compare.csv", "+w") as outfile:
        outfile.write(f"range,mr time,sqrt time\n")
        for j in powers_of_10:
            for k in [1, 2, 5]:
                for i in range(10 ** j * k + 1, 10 ** j  * k + interval_size + 1):
                    m_start = time.process_time_ns()
                    miller_first_k(i, 3)
                    miller_clock += time.process_time_ns() - m_start
                    s_start = time.process_time_ns()
                    sqrt_n(i)
                    sqrt_clock += time.process_time_ns() - s_start
                print("done with", i, j, k)
                outfile.write(f"{10 ** j * k + 1}-{10 ** j * k + interval_size},{miller_clock / 1e9},{sqrt_clock / 1e9}\n")
                outfile.flush()
                miller_clock = 0
                sqrt_clock = 0
            
def rabin_speed_test(miller_test_type: str, passes):
    miller_clock = 0.0
    interval_size = 100000
    powers_of_10 = list(range(5, 18))
    with open(f"{output_directory}/rabin_speed_{miller_test_type}_k{passes}.csv", "+w") as outfile:
        outfile.write(f"range,mr time\n")
        for j in powers_of_10:
            for k in [1, 2, 5]:
                for i in range(10 ** j * k, 10 ** j  * k + interval_size):
                    m_start = time.process_time_ns()
                    str_to_func[miller_test_type](i, passes)
                    miller_clock += time.process_time_ns() - m_start
                outfile.write(f"{10 ** j * k},{miller_clock / 1e9}\n")
                outfile.flush()
                miller_clock = 0
    print("done with", miller_test_type, passes)
    

def miller_verified_speed(miller_test_type: str):
    with open(f"{output_directory}/generated_up_to_miller_verified.csv", "+w") as up_to:
        with open(f"{output_directory}/generated_n_primes_miller_verified.csv", "+w") as n_primes:
            up_to.write("seconds,max int from k=1,max int from k=2, max int from k=3\n")
            n_primes.write("seconds,primes from k=1,primes from k=2, primes from k=3\n")
            for i in [1, 2, 5, 10, 30, 60, 120, 300]:
                k1 = generate_miller_verfied(str_to_func[miller_test_type], sqrt_n, 1, i)
                k2 = generate_miller_verfied(str_to_func[miller_test_type], sqrt_n, 2, i)
                k3 = generate_miller_verfied(str_to_func[miller_test_type], sqrt_n, 3, i)
                up_to.write(f"{i},{k1[0]},{k2[0]},{k3[0]}\n")
                n_primes.write(f"{i},{k1[1]},{k2[1]},{k3[1]}\n")
                print(f"Finished with {i} seconds per run")
                up_to.flush()
                n_primes.flush()

if __name__ == "__main__":
    if sys.argv[1] == "generate":
        prime_generation_tests()
    elif sys.argv[1] == "miller_acc":
        if len(sys.argv) <= 2:
            for size in ["small"]:#, "med", "large"]:
                for func in ["random", "random_k_range", "first_k"]:
                    miller_accuracy(func, size)
                    print(f"finished with", func, size)
        else:
            miller_accuracy(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "miller_speed":
        miller_speed("first_k")
    elif sys.argv[1] == "miller_ver_speed":
        miller_verified_speed("first_k")
    elif sys.argv[1] == "large_speed":
        large_primes_speed_test()
    elif sys.argv[1] == "rabin_speed":
        for func in ["random", "random_k_range", "first_k"]:
            for k in [1, 2, 3, 4]:
                rabin_speed_test(func, k)