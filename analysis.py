from tests import output_directory
import matplotlib.pyplot as plt
import numpy as np

def miller_acc():
    for size in ["small", "med", "large"]:
        print("size =", size)
        for func in ["random", "random_k_range", "first_k"]:
            print("function =", func)
            max_k = 3
            correct = [0] * max_k
            with open(f"{output_directory}/miller_{func}_{size}.csv", "r") as readfile:
                next(readfile)
                total = 0
                for line in readfile:
                    total += 1
                    for i in range(1, max_k + 1):
                        correct[i - 1] += int(line.strip().split(",")[i])
            for i in range(len(correct)):
                correct[i] = total - correct[i]
            print(correct, total)

def miller_time(passes):
    x = []
    y1 = []
    y2 = []
    y3 = []
    with open(f"{output_directory}/rabin_speed_{"random"}_k{passes}.csv", "r") as readfile:
        next(readfile)
        for line in readfile:
            data = line.strip().split(",")
            x.append(int(data[0]))
            y1.append(float(data[1]))
    with open(f"{output_directory}/rabin_speed_{"first_k"}_k{passes}.csv", "r") as readfile:
        next(readfile)
        for line in readfile:
            data = line.strip().split(",")
            y2.append(float(data[1]))
    with open(f"{output_directory}/rabin_speed_{"random_k_range"}_k{passes}.csv", "r") as readfile:
        next(readfile)
        for line in readfile:
            data = line.strip().split(",")
            y3.append(float(data[1]))
    
    plt.figure()
    plt.plot(x, y1, marker="o", linestyle="--", label="random")
    plt.plot(x, y3, marker="o", linestyle="--", label="random consecutive k")
    plt.plot(x, y2, marker="o", linestyle="--", label="first k")
    plt.xscale("log")
    plt.xlabel("Starting integer (log scale axis)")
    plt.ylabel("Seconds")
    plt.legend()
    plt.title("Miller-Rabin time to check 100,000 consecutive integers")
    plt.show()

def determ_n_primes():
    x = []
    naive = []
    sqrt = []
    sqrt_list = []
    with open(f"{output_directory}/generated_n_primes.csv", "r") as non_miller:
        next(non_miller)
        for line in non_miller:
            data = line.strip().split(",")
            x.append(int(data[0]))
            naive.append(int(data[1]))
            sqrt.append(int(data[2]))
            sqrt_list.append(int(data[3]))

    npx = np.array(x)
    npy_naive = np.array(naive)
    npy_sqrt = np.array(sqrt)
    npy_sqrt_list = np.array(sqrt_list)

    log_x = np.log10(npx)
    log_naive = np.log10(npy_naive)
    slope1, intercept1 = np.polyfit(log_x, log_naive, 1)
    log_sqrt = np.log10(npy_sqrt)
    slope2, intercept2 = np.polyfit(log_x, log_sqrt, 1)
    log_sqrt_list = np.log10(npy_sqrt_list)
    slope3, intercept3 = np.polyfit(log_x, log_sqrt_list, 1)
    
    x_fit = np.linspace(0, 3)
    
    plt.figure()
    plt.scatter(log_x, log_naive, marker="o", label="naive")
    plt.plot(x_fit, x_fit * slope1 + intercept1, linestyle="--", label=f"y={slope1:.2f}x + {intercept1:.2f}")
    plt.scatter(log_x, log_sqrt, marker="o", label="to sqrt(n)")
    plt.plot(x_fit, x_fit * slope2 + intercept2, linestyle="--", label=f"y={slope2:.2f}x + {intercept2:.2f}")
    plt.scatter(log_x, log_sqrt_list, marker="o", label="sqrt with prime list")
    plt.plot(x_fit, x_fit * slope3 + intercept3, linestyle="--", label=f"y={slope3:.2f}x + {intercept3:.2f}")
    plt.xlabel("Seconds allowed (log10)")
    plt.ylabel("Primes generated (log10)")
    plt.title("Primes generated in fixed time (log-log plot)")
    plt.legend()
    plt.show()

def determ_up_to():
    x = []
    naive = []
    sqrt = []
    sqrt_list = []
    with open(f"{output_directory}/generated_up_to.csv", "r") as non_miller:
        next(non_miller)
        for line in non_miller:
            data = line.strip().split(",")
            x.append(int(data[0]))
            naive.append(int(data[1]))
            sqrt.append(int(data[2]))
            sqrt_list.append(int(data[3]))

    

    npx = np.array(x)
    npy_naive = np.array(naive)
    npy_sqrt = np.array(sqrt)
    npy_sqrt_list = np.array(sqrt_list)

    log_x = np.log10(npx)
    log_naive = np.log10(npy_naive)
    slope1, intercept1 = np.polyfit(log_x, log_naive, 1)
    log_sqrt = np.log10(npy_sqrt)
    slope2, intercept2 = np.polyfit(log_x, log_sqrt, 1)
    log_sqrt_list = np.log10(npy_sqrt_list)
    slope3, intercept3 = np.polyfit(log_x, log_sqrt_list, 1)
    
    x_fit = np.linspace(0, 3)
    
    plt.figure()
    plt.scatter(log_x, log_naive, marker="o", label="naive")
    plt.plot(x_fit, x_fit * slope1 + intercept1, linestyle="--", label=f"y={slope1:.2f}x + {intercept1:.2f}")
    plt.scatter(log_x, log_sqrt, marker="o", label="to sqrt(n)")
    plt.plot(x_fit, x_fit * slope2 + intercept2, linestyle="--", label=f"y={slope2:.2f}x + {intercept2:.2f}")
    plt.scatter(log_x, log_sqrt_list, marker="o", label="sqrt with prime list")
    plt.plot(x_fit, x_fit * slope3 + intercept3, linestyle="--", label=f"y={slope3:.2f}x + {intercept3:.2f}")
    plt.xlabel("Seconds allowed (log10)")
    plt.ylabel("N (log10)")
    plt.title("Largest integer checked in fixed time (log-log plot)")
    plt.legend()
    plt.show()


def miller_vs_determ_n_primes():
    x = []
    naive = []
    sqrt = []
    sqrt_list = []
    # i-th entry is list for i + 1 passes
    miller_l = [[], [], []]
    miller_ver_l = [[], [], []]
    with open(f"{output_directory}/generated_n_primes.csv", "r") as non_miller:
        next(non_miller)
        for line in non_miller:
            data = line.strip().split(",")
            x.append(int(data[0]))
            naive.append(int(data[1]))
            sqrt.append(int(data[2]))
            sqrt_list.append(int(data[3]))
    with open(f"{output_directory}/generated_n_primes_miller.csv", "r") as miller:
        next(miller)
        for line in miller:
            data = line.strip().split(",")
            for i in [1, 2, 3]:
                miller_l[i-1].append(int(data[i]))
    with open(f"{output_directory}/generated_n_primes_miller_verified.csv", "r") as miller_ver:
        next(miller_ver)
        for line in miller_ver:
            data = line.strip().split(",")
            for i in [1, 2, 3]:
                miller_ver_l[i-1].append(int(data[i]))

    
    
    plt.figure()
    plt.plot(x, naive, marker="o", linestyle="-", label="naive")
    plt.plot(x, sqrt, marker="o", linestyle="-", label="to sqrt(n)")
    plt.plot(x, sqrt_list, marker="o", linestyle="-", label="sqrt with prime list")
    plt.plot(x, miller_l[0], marker="o", linestyle="-", label="miller rabin")
    plt.plot(x, miller_ver_l[0], marker="o", linestyle="-", label="miller rabin with prime verification")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Seconds allowed")
    plt.ylabel("Primes generated")
    plt.title("Primes generated in fixed time (log-log plot)")
    plt.legend()
    plt.show()

def selected_n_primes_lobf():
    x = []
    sqrt = []
    # i-th entry is list for i + 1 passes
    miller_l = []
    miller_ver_l = []
    with open(f"{output_directory}/generated_n_primes.csv", "r") as non_miller:
        next(non_miller)
        for line in non_miller:
            data = line.strip().split(",")
            x.append(int(data[0]))
            sqrt.append(int(data[2]))
    with open(f"{output_directory}/generated_n_primes_miller.csv", "r") as miller:
        next(miller)
        for line in miller:
            data = line.strip().split(",")
            miller_l.append(int(data[1]))
    with open(f"{output_directory}/generated_n_primes_miller_verified.csv", "r") as miller_ver:
        next(miller_ver)
        for line in miller_ver:
            data = line.strip().split(",")
            miller_ver_l.append(int(data[1]))

    npx = np.array(x)
    npy_sqrt = np.array(sqrt)
    npy_miller = np.array(miller_l)
    npy_miller_ver = np.array(miller_ver_l)

    log_x = np.log10(npx)
    log_sqrt = np.log10(npy_sqrt)
    slope1, intercept1 = np.polyfit(log_x, log_sqrt, 1)
    log_miller = np.log10(npy_miller)
    slope2, intercept2 = np.polyfit(log_x, log_miller, 1)
    log_miller_ver = np.log10(npy_miller_ver)
    slope3, intercept3 = np.polyfit(log_x, log_miller_ver, 1)
    
    x_fit = np.linspace(0, 4)
    
    plt.figure()
    plt.scatter(log_x, log_sqrt, marker="o", label="to sqrt(n)")
    plt.plot(x_fit, x_fit * slope1 + intercept1, linestyle="--", label=f"y={slope1:.2f}x + {intercept1:.2f}")
    plt.scatter(log_x, log_miller, marker="o", label="miller rabin")
    plt.plot(x_fit, x_fit * slope2 + intercept2, linestyle="--", label=f"y={slope2:.2f}x + {intercept2:.2f}")
    plt.scatter(log_x, log_miller_ver, marker="o", label="miller rabin with prime verification")
    plt.plot(x_fit, x_fit * slope3 + intercept3, linestyle="--", label=f"y={slope3:.2f}x + {intercept3:.2f}")
    plt.xlabel("log10 Seconds allowed")
    plt.ylabel("log10 Primes generated")
    plt.title("Log-log plot with lines of best fit")
    plt.legend()
    plt.show()

miller_time(3)
