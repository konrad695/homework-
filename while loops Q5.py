'''
Author: konrad
Date: 10/7/2025
Description:while loops
Q5
'''

num=1

while num != ' ':
    num = input('give me a number')
    if num.isdigit():
        num = int(num)
        for i in range (1,num**2):
            if i == 50:
                break
            print(i)