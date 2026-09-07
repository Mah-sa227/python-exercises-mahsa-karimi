'''
برای پیدا کردن کلمات انگلیسی یه عالمه سرچ کردم
 یه عالمه هم کد های
 ناموفق زدم و تمام تلاشم رو کردم
 اما نشد برای همین از چت جی پی تی راهنمایی گرفتم
 و توی گوگل هم سرچشون کردم
 ببخشید ولی در غیر اینصورت امکان حل برام وجود نداشت
'''


import re

word = input(' enter :  ')
english = re.findall(r'[a-zA-Z]+', word)

charachterha = sum(len(i) for i in english)
print('english letters : ', charachterha)
    
up = []
low = []
num = []
special =['!','@','#','$','%','&','*','_','?']
specialll = []
space = []

for i in word:
   
    if i.isupper():
        up += i
    
    if i.islower():
        low += i
        
    if i.isdigit():
        num += i
        
    if i in special:
        specialll +=i
        
    if i == ' ':
        space += i


print('uppercase : ', len(up))        

print('lowercase : ', len(low))

print('space : ', len(space))

print('numbers : ', len(num))

print('special : ', len(specialll))


