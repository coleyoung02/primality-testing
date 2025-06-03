
with open("P-1000000.txt", "r") as old_p:
    with open("primes.txt", "+w") as new_p:
        for line in old_p:
            new_p.write(line.split(",")[1].strip() + "\n")