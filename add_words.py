with open('bigdic.txt', 'r', encoding='utf8') as f:
    buffer = []
    main_words = {}
    sub_word = {}
    word = []
    sub_words = []
    while True:
        line = f.readline()
        if line != ' \n':
            if line.find(' | сущ ') != -1:
                buffer.append(line)
        else:
            if len(buffer) == 12:
                for item in buffer:
                    s_item = item.split('|')
                    word = s_item[0].strip()
                    options = s_item[1].strip().split()
                    if item.startswith('  '):
                        if not main_words.get('word_plural'):
                            sub_word['word'] = word
                            sub_word['word_case'] = options[-1]
                            sub_words.append(sub_word.copy())
                        else:

                            sub_word['word_plural'] = word
                            print('  ', word, options)
                    else:
                        if not main_words.get('word'):
                            sub_word['word'] = word
                            sub_word['word_case'] = options[-1]
                            sub_words.append(sub_word.copy())

                            main_words['word'] = word
                            main_words['is_nominal'] = 1
                            if options[3] == 'муж':
                                main_words['gender'] = 'М'
                            elif options[3] == 'жен':
                                main_words['gender'] = 'Ж'
                            else:
                                main_words['gender'] = 'С'
                            if options[1] == 'неод':
                                main_words['is_animate'] = 0
                            else:
                                main_words['is_animate'] = 1
                        else:
                            main_words['word_plural'] = word
                        print(word, options)
            else:
                pass
            buffer = []
        if 1 < 0:
            break

#TODO Убрать два поля, доделать это дерьмо нах