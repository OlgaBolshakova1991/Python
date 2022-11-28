import model
import view
import operation
import log

def button_click():
    some_str = view.inp()
    some_tuple = operation.op(some_str)
    model.init(some_tuple[0], some_tuple[1])

    if some_tuple[2] == '+':
        result = model.sum()
    elif some_tuple[2] == '-':
        result = model.dif()
    elif some_tuple[2] == '*':
        result = model.mult()
    elif some_tuple[2] == '/':
        result = model.div()
    else:
        view.view_data('Такой операции не существует')
    
    view.view_data(f'Результат равен {result}')

    log.write(some_str, result)