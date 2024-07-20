from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
        sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
function_time = time_end - time_start
print(f'Затраченное время 4 функций: {function_time}')

time_start = datetime.now()

trh_1 = Thread(target=write_words, args=(10, 'example5.txt'))
trh_2 = Thread(target=write_words, args=(30, 'example6.txt'))
trh_3 = Thread(target=write_words, args=(200, 'example7.txt'))
trh_4 = Thread(target=write_words, args=(100, 'example8.txt'))

trh_1.start()
trh_2.start()
trh_3.start()
trh_4.start()

trh_1.join()
trh_2.join()
trh_3.join()
trh_4.join()

time_end = datetime.now()
thread_time = time_end - time_start
print(f'Затраченное время 4 потоков: {thread_time}')
