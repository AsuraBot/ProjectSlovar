with open('bigdic.txt', 'r', encoding='utf8') as f:
    count = 0
    buffer = []
    main_words = {}
    sub_words = {}
    while True:
        line = f.readline()
        if line != ' \n':
            if line.find(' | сущ ') != -1:
                buffer.append(line)
        else:
            if len(buffer) == 12:
                for item in buffer:
                    if item.startswith('  '):
                        s_item = item.split('|')
                        print('  ', s_item[0].strip())
                    else:
                        count += 1
                        s_item = item.split('|')
                        print(s_item[0].strip())
            else:
                pass
            buffer = []
        if count < 0:
            break

#TODO Собрать данные о слове (род, падеж, неодушевленнность)