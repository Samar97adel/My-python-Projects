name=input('Enter your name=')
score=int(input('Enter your score'))
if score>=90:
    print('Student name is ',name ,'score is ', score , 'and your grade is A')
elif score>=80 and score<90:
        print('Student name is ',name,'score is ', score, 'and your grade is B')
elif score >=70 and score<80:
        print('Student name is ',name,'score is ', score ,'and your grade is C')
elif score>=50 and score<70:
        print('Student name is ',name ,'score is ',score , ' and your grade is D')
else:
        print('Student name is ',name ,'scoreis ',score , 'and your grade is fail')




