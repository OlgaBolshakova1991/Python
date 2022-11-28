import datetime
def write (some_str, result):
    with open('log.txt', 'a', encoding = 'utf-8') as l:
        l.write(f'{some_str} = {result}. Время запроса: {datetime.datetime.now()}' + '\n')