import os

def read_last_line():
    with open('output','r') as f:
        line = f.read().splitlines()
        last_line = line[-1]
        return last_line

lisp_code = ""

# def close_brackets(input_line):
#     #operators = {'+':'b','*':'b','s':'b'}
#     operators = ['+','s','*']
#     ignore = ['-']
#     global lisp_code
#     if input_line[0] == '':
#         return ''
#     if input_line[0] in operators:
#         lisp_code = lisp_code + close_brackets(input_line[1:])
#     elif input_line[0] not in operators and input_line[0] not in ignore:
#         lisp_code = lisp_code + input_line[0] + close_brackets(input_line[1:]) + ")"
#     if input_line[0] == 'q':
#         return lisp_code + ')'

# required_line = []
# def close_brackets(input_line):
#     input_line = list(input_line)
#     global required_line
#     operators = ['+','s','*']
#     if input_line[0] in operators:
#         required_line = required_line.extend(close_brackets(input_line[1:]))
#     elif input_line[0] not in operators and input_line[0] !='-':
#         required_line = required_line.extend(close_brackets[2:]).append(')')
#     if input_line[0] == 'q':
#         return ''.join(required_line)
os.system("python GP.py > output")
main_line = read_last_line()
main_line = main_line.replace('add','(+')
main_line = main_line.replace('mul','(*')
main_line = main_line.replace('sub','(s')

main_line = main_line.replace('+)','+')
main_line = main_line.replace('s)','s')
main_line = main_line.replace('*)','*')

main_line = main_line.replace('s','-')




#main_line=main_line.replace('s','-')
#main_line = main_line + ')'

#main_line = close_brackets(main_line)
print(main_line)

