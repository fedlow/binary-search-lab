import random
from binary_search import binary_search

random.seed(42)

arr = sorted(random.sample(range(1, 1001), 100))

print("Отсортированный список из 100 чисел:")
print(arr)
print()

targets = [
    arr[0],
    arr[25],
    arr[50],
    arr[75],
    arr[-1],
    -10,
    5000,
    777,
]

print("Результаты бинарного поиска:")
for target in targets:
    index = binary_search(arr, target)
    if index != -1:
        print(f"Значение {target} найдено по индексу {index}")
    else:
        print(f"Значение {target} не найдено, результат = -1")