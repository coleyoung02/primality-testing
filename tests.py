from primality_test import *
from utils import generate_primes, read_primes
import const
import sys

output_directory = "test_outputs"


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
    str_to_func = {"random": miller_randoms, "random_k_range": miller_random_plus_k_range, "first_k": miller_first_k}
    size_to_bounds = {"small": (const.SMALL_LOW, const.SMALL_HI), 
                      "med": (const.MED_LOW, const.MED_HI), 
                      "large": (const.LOW, const.HI)}
    low = size_to_bounds[size][0]
    hi = size_to_bounds[size][1]
    test = str_to_func[miller_test_type]
    primes = read_primes("primes.txt")

    with open(f"{output_directory}/miller_{miller_test_type}_{size}.csv", "+w") as test_out:
        test_out.write("n,k=1,k=2,k=3,k=4")
        for i in range(low, hi):
            if (i % ((hi - low) // 10)) == 0:
                print("finished", i)
            line = f"{i},"
            for k in range(1, 6):
                line += str(int(test(i, k) == (i in primes))) + ","
            test_out.write(line[:-1] + "\n")
            


if __name__ == "__main__":
    if sys.argv[1] == "generate":
        prime_generation_tests()
    elif sys.argv[1] == "miller_acc":
        if len(sys.argv) <= 2:
            for size in ["small", "med", "large"]:
                for func in ["random", "random_k_range", "first_k"]:
                    miller_accuracy(func, size)
                    print(f"finished with", func, size)
        else:
            miller_accuracy(sys.argv[2], sys.argv[3])
