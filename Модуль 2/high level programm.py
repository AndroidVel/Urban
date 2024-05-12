from random import randrange
number = randrange(18) + 3
print(number)
s = ''
for i in range(1, number // 2 + 1):
    for j in range(1, 20):
        summ = i + j
        if number % summ == 0 and i != j and i < j:
            s += str(i) + str(j)
print(int(s))
