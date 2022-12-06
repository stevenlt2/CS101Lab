print('**** Welcome to the LAB grade calculator! ****')
print()

user_name = input('Who are we calculating grades for? ==>')
print()
user_labgrade = int(input('Enter the Labs grade? ==>'))
if user_labgrade > 100:
    print('The lab value should have been 100 or less. It has been changed to 100.')
    user_labgrade = 100
print()
user_examsgrade = int(input('Enter the EXAMS grade? ==>'))
if user_examsgrade < 0:
    print('The exam value should have been zero or greater. It has been changed to zero')
    user_examsgrade = 0
    
print()
user_attend = int(input('Enter the Attendance grade? ==>'))
print()
user_weighted = (user_labgrade * 0.7) + (user_examsgrade * 0.2) + (user_attend * 0.1)
print('The weighted grade for', user_name, 'is', user_weighted)
if user_weighted >= 90:
    print(user_name,'has a letter grade of A')
elif user_weighted >= 80:
    print(user_name ,'has a letter grade of B')
elif user_weighted >= 70:
    print(user_name ,'has a letter grade of C')
elif user_weighted >= 60:
    print(user_name ,'has a letter grade of D')
else:
    print(user_name ,'has a letter grade of F')




print()
print('**** Thanks for using the Lab grade calculator ****')

