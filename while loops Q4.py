'''
Author: konrad
Date: 10/7/2025
Description:while loops
Q4
'''

num=1

while num != ' ':
    num = input('give me a number')
    if num.isdigit():
        num = int(num)
        for i in range (1,num):
            if (i%5 == 0):
                continue
            else:
                print(i)
                
    