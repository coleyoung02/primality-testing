from tests import output_directory

def miller_anal():
    for size in ["small", "med", "large"]:
        for func in ["random", "random_k_range", "first_k"]:
            max_k = 3
            correct = [0] * max_k
            with open(f"{output_directory}/miller_{func}_{size}.csv", "r") as readfile:
                next(readfile)
                total = 0
                for line in readfile:
                    total += 1
                    for i in range(1, max_k + 1):
                        correct[i - 1] += int(line.strip().split(",")[i])
            print(correct, total)

miller_anal()
