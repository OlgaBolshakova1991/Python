from datetime import datetime as dt


def log_operation(operation):
    time = dt.now().strftime('%D  %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as f:
        f.write(f"{time}  {operation}\n")
