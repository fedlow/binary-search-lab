import random
from binary_search import binary_search

random.seed(42)

arr = sorted(random.sample(range(1, 1001), 100))

targets = [
    arr[0], arr[25], arr[50], arr[75], arr[-1],
    -10, 5000, 777,
]

lines = []
lines.append("Отсортированный список из 100 чисел:")
lines.append(str(arr))
lines.append("")
lines.append("Результаты бинарного поиска:")
for target in targets:
    index = binary_search(arr, target)
    if index != -1:
        lines.append(f"Значение {target} найдено по индексу {index}")
    else:
        lines.append(f"Значение {target} не найдено, результат = -1")

text = "\n".join(lines)

print(text)

with open("task_03_output.txt", "w", encoding="utf-8") as f:
    f.write(text)