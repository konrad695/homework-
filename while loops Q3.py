'''
Author: konrad
Date: 10/7/2025
Description:while loops
Q3
'''

num=1

while num != ' ':
    num = input('give me a number')
    if num.isdigit():
        num = int(num)
        for i in range (0,num):
            if (i%2  == 0):
                print(i)
                