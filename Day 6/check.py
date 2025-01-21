import multiprocessing
from math import factorial
from decimal import Decimal, getcontext
import time

def calculate_e(k_start, k_end, que=None):
    getcontext().prec = 100
    partial_sum = Decimal(0)

    for k in range(k_start, k_end):
        partial_sum += Decimal(1) / Decimal(factorial(k))

    if que is not None:
        que.put(partial_sum)
    else:
        return partial_sum

if __name__ == "__main__":
    N = 1000                     
    threads_count = 4            
    getcontext().prec = 100     

    num_cores = multiprocessing.cpu_count()
    print(f"Number of cores: {num_cores}")

    chunk_size = (N + threads_count - 1) // threads_count
    calc_chunks = [(i * chunk_size, min((i + 1) * chunk_size, N)) for i in range(threads_count)]

    start_time = time.time()

    queue = multiprocessing.Queue()
    processes = []

    for start, end in calc_chunks:
        process = multiprocessing.Process(target=calculate_e, args=(start, end, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    e_approximation = Decimal(0)
    while not queue.empty():
        e_approximation += queue.get()

    end_time = time.time()

    print(f"Calculated value of e: {e_approximation}")
    print(f"Elapsed time: {end_time - start_time:.2f} seconds")
