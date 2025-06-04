from primality_test import generate_primes, naive, sqrt_n, sqrt_n_list
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



if __name__ == "__main__":
    if sys.argv[1] == "generate":
        prime_generation_tests()
    elif sys.argv[1] == "miller_acc":
        pass