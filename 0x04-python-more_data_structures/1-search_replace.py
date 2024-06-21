#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ne_list=[]
    for i in range(len(my_list)) :
        ne_list.append(my_list[i])
        
    for i in range(len(ne_list)) :
        if ne_list[i] == search :
            ne_list[i] = replace
    return(ne_list)
