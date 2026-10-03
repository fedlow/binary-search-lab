import random
import time
import matplotlib.pyplot as plt
from binary_search import binary_search, linear_search


def measure_avg(func, arr, targets, repeats=200):
    total = 0.0

    for target in targets:
        start = time.perf_counter()
        for _ in range(repeats):
            func(arr, target)
        total += time.perf_counter() - start

    return total / (len(targets) * repeats)


def main():
    random.seed(42)

    sizes = [100, 200, 500, 1000, 2000, 5000, 10000]
    binary_times = []
    linear_times = []

    for n in sizes:
        population = range(1, n * 10 + 1)
        arr = sorted(random.sample(population, n))

        targets = [
            arr[0],
            arr[n // 4],
            arr[n // 2],
            arr[3 * n // 4],
            arr[-1],
            -1,
            n * 10 + 1,
        ]

        bt = measure_avg(binary_search, arr, targets, repeats=200)
        lt = measure_avg(linear_search, arr, targets, repeats=200)

        binary_times.append(bt)
        linear_times.append(lt)

        print(f"n={n:6d} | binary={bt:.8f} c | linear={lt:.8f} c")

    # График
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, binary_times, marker="o", label="Бинарный поиск")
    plt.plot(sizes, linear_times, marker="s", label="Линейный поиск")
    plt.xlabel("Размер списка n")
    plt.ylabel("Среднее время выполнения, сек")
    plt.title("Бинарный поиск vs линейный поиск")
    plt.legend()
    plt.grid(True)
    plt.savefig("search_comparison.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()