# Файл с уже/еще ненужными функциями
import sqlite3
import re


def insert_in_db(cursor):
    """
    Добавить в БД
    """
    with open('word_rus.txt', 'r', encoding='utf-8') as f:
        words = f.read()
        for word in words.split('\n'):
            print(word)
            try:
                cursor.execute("INSERT INTO WORDS (WORD) VALUES (?)", (word,))
            except sqlite3.IntegrityError:
                continue


# Ввод числа для поиска слов
while True:
    try:
        word_len = input("Ведите количество букв: ")
        if word_len <= 1:
            raise ValueError()
    except ValueError:
        print("Введите положительное число больше 1!")
    else:
        break


def length_search(cursor, word_len):
    """
    Поиск по длине слова
    """
    cursor.execute('''
        SELECT word FROM words WHERE LENGTH(word) = ?
    ''', (word_len,))
    return cursor.fetchall()


def letter_search(cursor, letters):
    """
    Поиск по буквам
    """
    clean_letters = re.findall(r'[а-яА-Я]', letters)
    mask_letters = '%{}%'.format('%'.join(clean_letters))
    cursor.execute('''
        SELECT word FROM words WHERE word LIKE ?
    ''', (mask_letters,))
    return cursor.fetchall()
