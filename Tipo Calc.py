# Вычислить значение выражения:
# 12 + 15
# 12 / 15
# 112 * 15


# 1. Где операторы?
# 2. Где числовые значения?


# Уровень 1:

# - 1 действие
# - 2 аргумента

# Уровень 2:

# - Количество действие произвольное
# 12 + 15 - 4


# Уровень 3:
# - Действия имеют приоритет

# 12 - 4*2

# Уровень 4:
# - Действия разделяются скобками

# (12 - 4) * 2


n = '22 * 300 - 14 + 10 * 10'
m = n.split()
m2 = []
print(m)


def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b


# a = int(m[0])
# c = m[1]
# b = int(m[2])

# result = calc(a, b, c)

result = int(m[0])


# def calc_row(result):
for i in range(1, len(m) - 1, 2):
    if m[i] == '*' or m[i] == '/':
     result = calc(int(m[i - 1]), int(m[i + 1]), m[i])
     m2.append(result)
    else:
         m2.append(m[i])
         m2.append(int(m[i + 1]))
     
print(m[i], m[i + 1])
print(m2)
print(result)
 

