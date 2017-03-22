import multiprocessing as mp

output = mp.Queue()


# An example function to check parallel execution and speedup
def solve(k, pos, output):
    sum = 0
    for i in xrange(1000000):
        sum += k
        sum %= 123444
    output.put((pos, sum))


# Just reading a file with T+1 numbers.
# The first has the number T and
# the next T contain the T testcases.
T = int(raw_input())
processes = []
for t in range(1, T + 1):
    data = int(raw_input())
    process = mp.Process(target=solve, args=(data, t, output), )
    processes.append(process)

# Here is the parallel execution.
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
