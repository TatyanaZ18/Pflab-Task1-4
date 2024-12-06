import sys

def circular_array(n, m):
    nums_arr = list(range(1, n + 1))
    path = []  # Список для хранения пути
    index = 0  # Текущий индекс, начинаем с 0
    path.append(nums_arr[index])
    while (index + m - 1) % n != 0:
        index = (index + m - 1) % n
        path.append(nums_arr[index])
    return ''.join(map(str, path))

n = int(sys.argv[1])
m = int(sys.argv[2])

print(circular_array(n, m))
