grade= 2

count= 0

total= 0
 
while grade != '' :

    grade= input('Enter your grade: ')

    if grade.isdigit():

        grade=int(grade)

        total= total+grade

        count+=1

average= (total/count)

print(average)
 
if average >= 90:

    print('A,you passed')

elif (average <= 89) and (average >=80):

    print('B,you passed')

elif (average <=79) and (average >=70):

    print('C,you passed')

elif (average <=69) and (average >=60):

    print('D,you passed')

elif (average <=59):

    print('F,you failed')

else:

    print(' not right')
 