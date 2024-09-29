import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()


cursor.execute('DELETE FROM Users WHERE username = ?', ('User6',))

cursor.execute('SELECT SUM(balance) FROM Users')
sum_ = cursor.fetchone()[0]

cursor.execute('SELECT COUNT(*) FROM Users')
count = cursor.fetchone()[0]

print(sum_/count)

connection.commit()
connection.close()
