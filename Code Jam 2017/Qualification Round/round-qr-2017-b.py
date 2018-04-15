import multiprocessing as mp

output = mp.Queue()


def is_tidy(n):
    digits = str(n)
    return digits == ''.join(sorted(digits))


# An example function to check parallel execution and speedup
def find_tidy(n, pos, output):
    if is_tidy(n):
        output.put((pos, n))
        return
    digits = str(n)
    while True:
        idx = 0
        for i in xrange(len(digits)):
            if digits[i] > digits[i + 1]:
                idx = i
                break
        new_digits = [digits[i] if i <
                      idx else '9' for i in xrange(len(digits))]
        new_digits[idx] = str(int(digits[idx]) - 1)
        res = int(''.join(new_digits))
        if is_tidy(res):
            output.put((pos, res))
            return
        else:
            digits = new_digits


T = int(raw_input())
processes = []
for t in range(1, T + 1):
    n = int(raw_input())
    process = mp.Process(target=find_tidy, args=(n, t, output))
    processes.append(process)

# Parallel execution.
cpus = mp.cpu_count()
for idx in xrange(0, T, cpus):
    for p in xrange(idx, min(idx + cpus, T)):
        processes[p].start()

    for p in xrange(idx, min(idx + cpus, T)):
        processes[p].join()

# Receiving the results.
results = [output.get() for p in processes]
results.sort()

# Formatting the results as needed.
out_str = 'Case #{0}: {1}\n'
print_res = map(lambda x: out_str.format(x[0], x[1]), results)

# Printing the results.
print(''.join(print_res))
