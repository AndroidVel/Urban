from pprint import pprint
import zipfile
from random import randint

# file_name = 'voina_i_mir.zip'
# zfile = zipfile.ZipFile(file_name, mode='r')
# for filename in zfile.namelist():
#     print(filename)
#     zfile.extract(filename)


stat = {}

sequence = ''
file_name = 'voina-i-mir.txt'
with open(file_name, mode='r', encoding='cp1251') as file:
    for line in file:
        file = file[:-1]
        # print(line)
        for char in line:
            if sequence in stat:
                if char in stat[sequence]:
                    stat[sequence][char] += 1
                else:
                    stat[sequence][char] = 1
            else:
                stat[sequence] = {char: 1}
            sequence = sequence[1:] + char
# pprint(stat)

totals = {}
stat_for_generate = {}
for sequence, char_stats in stat.items():
    totals[sequence] = 0
    stat_for_generate[sequence] = []
    for char, count in char_stats.items():
        totals[sequence] += count
        stat_for_generate[sequence].append([count, char])
    stat_for_generate[sequence].sort(reverse=True)


n = 1000
printed = 0

sequence = ' '
while printed < n:
    char_stats = stat_for_generate[sequence]
    total = totals[sequence]
    dice = randint(1, total)
    pos = 0
    for count, char in char_stats:
        pos += count
        if dice <= pos:
            break
    print(char, end='')
    sequence = sequence[1:] + char
    printed += 1
