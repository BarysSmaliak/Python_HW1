# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

Num = int(input("Введите число: "))
print("Сумма цифр этого числа равна", Num//100 + Num//10%10 + Num%10)