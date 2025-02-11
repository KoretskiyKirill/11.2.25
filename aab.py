import time
import itertools
from itertools import permutations
lst = ["A","A","B"]
lst2 = []
lst1 = []
for element in lst:
    lst1.append(ord(element))
for element in lst:
    lst2.append(ord(element))

def johnson_trotter(lst):
    q = 0
    n = len(lst)
    perm = lst[:]  # передача списка
    direction = [-1] * n  # -1 — движение влево, 1 — вправо

    def get_largest_mobile():
        largest = -1
        index = -1
        for i in range(n):
            new_pos = i + direction[i]
            if 0 <= new_pos < n and perm[i] > perm[new_pos] and perm[i] > largest:
                largest = perm[i]
                index = i
        return index
    perm2 = []
    while True:
        perm1 = []
        for element in perm:
            perm1.append(chr(element))
        print(perm1)

        k = get_largest_mobile()
        if k == -1:
            return  # проверка об окончании перерстановок

        # перестановка
        new_pos = k + direction[k]
        perm[k], perm[new_pos] = perm[new_pos], perm[k]
        direction[k], direction[new_pos] = direction[new_pos], direction[k]

        # Инвертирование направления
        for i in range(n):
            if perm[i] > perm[new_pos]:
                direction[i] *= -1
        q += 1
start = time.perf_counter()
johnson_trotter(lst1)
end = time.perf_counter()
print(end-start)
def narayani(arr):

    result = []
    def perestanivka(j):
        if j == len(arr):
            result.append(arr.copy())
            return
        for i in range(j, len(arr)):
            arr[j], arr[i] = arr[i], arr[j]
            perestanivka(j + 1)
            arr[j], arr[i] = arr[i], arr[j]

    perestanivka(0)
    return result
start_time = time.perf_counter()
e = 0
for perm in narayani(lst):
    if e == 0 or e == 1 or e == 5:
        print(perm)
    e += 1
end_time = time.perf_counter()
print(end_time-start_time, "секунд")









start_time = time.perf_counter()
e = 0
for p in permutations(lst):
    if e == 0 or e == 1 or e == 5:
        print(p)

    e += 1
end_time = time.perf_counter()
print(end_time-start_time, "секунд")