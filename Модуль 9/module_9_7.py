def is_prime(func):
    def wrapper(a, b, c):
        summ = func(a, b, c)

        # Проверка числа
        flag = False
        if summ == 1:
            print(summ, "Не простое число")
        elif summ > 1:
            for i in range(2, summ // 2):
                if (summ % i) == 0:
                    flag = True
                    break
            if flag:
                print("Составное")
            else:
                print("Простое")
        return summ
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
