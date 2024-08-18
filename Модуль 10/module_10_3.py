from random import randrange
from time import sleep
from threading import Thread, Lock


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            random_int = randrange(50, 500)
            self.balance += random_int
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {random_int}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            random_int = randrange(50, 500)
            print(f'Запрос на {random_int}')
            if self.balance >= random_int:
                self.balance -= random_int
                print(f'Снятие: {random_int}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
