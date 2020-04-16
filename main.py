import sqlite3
import re


def search(cursor, word_len=None, letters=None):
    sql = 'SELECT word FROM words WHERE 1 = 1'
    params = []

    if letters:
        clean_letters = re.findall(r'[а-яА-Я]', letters)
        if clean_letters:
            mask_letters = '%{}%'.format('%'.join(clean_letters))
            sql = sql + ' AND word LIKE ?'
            params.append(mask_letters)

    if word_len:
        sql = sql + ' AND LENGTH(word) = ?'
        params.append(word_len)

    cursor.execute(sql, params)
    return cursor.fetchall()


connection = sqlite3.connect('dictionary.db')
cursor = connection.cursor()


while True:
    # Ввод числа для поиска слов
    try:
        word_len = int(input("Введите количество букв: "))
    except ValueError:
        word_len = None

    # Ввод букв для поиска слов
    letters = input("Введите буквы: ")

    res = search(cursor, word_len, letters)
    for item, in res:
        print(item)

connection.commit()
connection.close()
