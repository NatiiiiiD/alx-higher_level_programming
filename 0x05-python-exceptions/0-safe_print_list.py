#!/usr/bin/python3
def safe_print_list(the_list=[], x=0):
    cmpt = 0
    for index in range(x):
        try:
            print(the_list[index], end='')
            cmpt += 1
        except Exception as error:
            break
    print('')
    return cmpt
