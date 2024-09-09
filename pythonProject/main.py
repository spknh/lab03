from random import randint
def bubble (a,k ):
    if k==0 :
        for i in range(N - 1):
            for j in range(N - 1 - i):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a
    if k==1:
        for i in range(N -1):
            for j in range( N-1-i):
                if a[j]<a[j+1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a

N = int(input("Введите массив числа:"))
a = []
for i in range(N):
    a.append(randint(1, 99))

print(a)  # вывод исходного неотсортированного списка

k = int(input("Как сортируем? \n 0 -  по возрастанию \n 1 - по убыванию \n"))
print(bubble(a, k))  # вывод отсортированного списка