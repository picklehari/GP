import os

def read_last_line():
    with open('output','r') as f:
        line = f.read().splitlines()
        last_line = line[-1]
        return last_line

lisp_code = ""

def close_brackets(input_line):
    operators = {'+':'b','*':'b','s':'b'}
    ignore = ['-']
    global lisp_code
    if input_line[0] in list(operators.keys()):
        lisp_code = lisp_code + close_brackets(input_line[1:])
    elif input_line[0] not in operators.keys() and input_line[0] not in ignore:
        lisp_code = lisp_code + input_line[0] + close_brackets(input_line[1:]) + ")"
    if input_line[0] == 'q':
        return lisp_code + ')'
    
def open_brackets(input_line):
    operators = {'+':'b','*':'b','s':'b'}
    for i in input_line:
        if i in list(operators.keys()) :
            input_line = input_line.replace(i, '(' + i)
        else:
            continue
    input_line = input_line.replace('s','-')
    return input_line
                     





os.system("python GP.py > output")
main_line = read_last_line()
main_line = main_line.replace('add','+')
main_line = main_line.replace('mul','*')
main_line = main_line.replace('sub','s')
main_line = main_line + 'q'
#main_line=main_line.replace('s','-')
#main_line = main_line + ')'

main_line = close_brackets(main_line)
main_line = open_brackets(main_line)
print(main_line)

