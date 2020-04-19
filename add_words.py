import sqlite3


def get_nouns(cursor):
    with open('bigdic.txt', 'r', encoding='utf8') as f:
        buffer = []
        sub_words = []
        for line in f:
            if line != ' \n':
                if line.find(' | сущ ') != -1:
                    buffer.append(line)
            else:
                if len(buffer) == 12:
                    word_info = {}
                    for i, item in enumerate(buffer[:6]):
                        sub_word = {}
                        s_item = item.split('|')
                        word = s_item[0].strip()
                        options = s_item[1].strip().split()
                        sub_word['word'] = word
                        sub_word['word_case'] = options[-1].strip()
                        word_plural = buffer[i+6].split('|')[0].strip()
                        sub_word['word_plural'] = word_plural
                        sub_words.append(sub_word.copy())

                    s_item = buffer[0].split('|')
                    options = s_item[1].strip().split()
                    word_info['is_nominal'] = 1
                    if options[3] == 'муж':
                        word_info['gender'] = 'М'
                    elif options[3] == 'жен':
                        word_info['gender'] = 'Ж'
                    else:
                        word_info['gender'] = 'С'
                    if options[1] == 'неод':
                        word_info['is_animate'] = 0
                    else:
                        word_info['is_animate'] = 1

                    cursor.execute("INSERT INTO NOUNS_INFO (GENDER, IS_ANIMATE, IS_NOMINAL) VALUES (?,?,?)",
                                   (word_info['gender'], word_info['is_animate'], word_info['is_nominal']))
                    pk = cursor.lastrowid

                    for item in sub_words:
                        print(item)
                        try:
                            cursor.execute("INSERT INTO NOUNS (WORD, WORD_CASE, WORD_PLURAL, NOUN_INFO_FK) VALUES (?,?,?,?)",
                                           (item['word'], item['word_case'], item['word_plural'], pk))
                        except sqlite3.IntegrityError:
                            raise
                    # cursor.commit()

                else:
                    print('buffer != 12')
                buffer = []
                sub_words = []
