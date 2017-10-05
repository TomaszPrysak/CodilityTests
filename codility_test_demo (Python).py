# -*- coding: utf-8 -*-

def solution(list):
    a = max(list)
    b = 1
    for i in range(0, len(list)):
        if (b < a) and (b not in list):
            break
        elif (b == a):
            b = b + 1
            break
        elif (b not in list):
            break            
        b = b + 1
    return b

A = [-10,-3,0,1,2,3,4,5,6,8,3,4,2]

B = [1,2,3,4]

C = [-5, -1, 0]

print(solution(A))
