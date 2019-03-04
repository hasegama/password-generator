# coding: utf-8

import os, sys
import numpy as np
import random

def pw_gen(length):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    lowers = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'        
        ]
    uppers = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
        ]
    marks = [
        '!','\"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~'
        ]
    letters = numbers+lowers+uppers+marks
    password = []
    for l in range(length):
        password.append(random.choice(letters))
    return password

if __name__=='__main__':
    random.seed(20190228)
    length=6
    for r in range(100):
        password = pw_gen(length)
        for l in range(length):
            print(password[l], end='')
        print()
    print('--------------------------------------------------')
