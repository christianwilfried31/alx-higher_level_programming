#!/usr/bin/python3
def safe_print_list(my_list=[], x=0) :
    to = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            to += 1
        except IndexError:
            break
    print()
    return (to)
