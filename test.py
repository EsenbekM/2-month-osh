from random import randint


def bubble_sort(list_):
    num = list_.copy()
    check = 1
    while check == 1:
        check = 0
        for x, i in enumerate(num):
            if x < len(num) - 1:
                if i > num[x + 1]:
                    var = num[x + 1]
                    num[x + 1] = i
                    num[x] = var
                    check = 1
    return num


def binary_search(var, num):
    first = 0
    last = len(num) - 1
    while True:
        middle = (first + last) // 2
        if var == num[middle]:
            print("Элемент найден: ", middle)
            break
        else:
            if var < num[middle]:
                last = middle - 1
            else:
                first = middle + 1
        if first > last:
            print("Элемент не найден.")
            break


numbers = [randint(0, 100) for i in range(randint(10, 30))]
print(f'Создан список длинной {len(numbers)}:')
print(numbers)
numbers2 = bubble_sort(numbers)
print('Список отсортирован:')
print(numbers2)
to_find = numbers[randint(0, len(numbers)-1)]
print(f"Ищем число: {to_find}")
binary_search(to_find, numbers2)

