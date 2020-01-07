import os
import re

def read_last_line():
    with open('output','r') as f:
        line = f.read().splitlines()
        last_line = line[-1]
        return last_line

os.system("python GP.py > output")
main_line = read_last_line()
main_line = main_line.replace('-','$')
main_line = main_line.replace('add','+')
main_line = main_line.replace('mul','*')
main_line = main_line.replace('sub','-')

operator_stack = {"+":2,"*":2,"-":2}
code_stack = []
operators=list(operator_stack.keys())

def tree_to_expression(tree,tree_size,i=0):
    if tree[i] in operators:
        code_stack.append('(')
        code_stack.append(tree[i])
        if tree[i+1] not in operators:
            code_stack.append(tree[i+1])
        else: 
            tree_to_expression(tree,tree_size-1,i=i+1)
        if tree[i+2] not in operators:
            code_stack.append(tree[i+2])
            code_stack.append(")")
        else: 
            tree_to_expression(tree,tree_size-2,i=i+2) 

def stack_update():
    flag = 0
    # for c in main_line:
    #     if c in operator_stack:
    #         code_stack.append('(')
    x = main_line.split()
    exp_length = len(x) - 2
    tree_to_expression(x,exp_length-2)
    return " ".join(code_stack)

main_line = stack_update()
main_line=main_line.replace("$","-")
# main_line = main_line.replace('add','+')
# main_line = main_line.replace('mul','*')
# main_line = main_line.replace('sub','-')
# main_line = main_line.replace('+)','+')
# main_line = main_line.replace('s)','s')
# main_line = main_line.replace('*)','*')
# main_line = main_line.replace('s','-')
# #main_line=main_line.replace('s','-')
# #main_line = main_line + ')'

# #main_line = close_brackets(main_line)
#print(main_line)

with open("output.lisp",'w+') as f:
    line = "(defun polynomial(x)" + main_line + "))"
    line_2 = "(write (polynomial 5))"
    f.write(line)
    f.write(line_2)
