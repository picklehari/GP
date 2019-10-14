def read_last_line():
    with open('output','r') as f:
        line = f.read().splitlines()
        last_line = line[-1]
        return last_line

def close_brackets():
    return


main_line = read_last_line()
main_line = main_line.replace('add','(+')
main_line = main_line.replace('mul','(*')
main_line = main_line.replace('sub','(s')

main_line=main_line.replace('s','-')
#main_line = main_line + ')'
print(main_line)

