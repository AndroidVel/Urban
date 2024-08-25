import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file.readlines():
            if line:
                all_data.append(line)
            else:
                break


file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

time_start = datetime.datetime.now()
for filename in file_names:
    read_info(filename)
time_end = datetime.datetime.now()
print(f'Линейный вызов занял {time_end - time_start}')

if __name__ == '__main__':
    time_start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    time_end = datetime.datetime.now()
    print(f'Многопроцессный занял {time_end - time_start}')
