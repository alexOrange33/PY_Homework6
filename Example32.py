#  Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)

def Fill_Array_From_Console():
    n = int(input("Введите количество элементов: "))
    list_1 = list()
    for i in range(n):
        list_1.append(int(input(f"Введите {i} элемент: ")))
    return list_1

min = int(input("Введите min: "))
max = int(input("Введите max: "))
list_1 = Fill_Array_From_Console()
print(list_1)
for i in range(0,len(list_1)):
    if list_1[i] >= min and list_1[i] <= max:
        print(i)