import random

r=random.randint(1,10)

while True:
    guess=int(input('Guess a number : '))
    
    if guess>r:
        print('عدد را کوچکتر کن')
        continue
    
    elif guess < r:
         print('عدد را بزرگتر کن')
         continue
     
    else: 
        guess==r
        print('تبریک شما موفق شدید ')
        break
    