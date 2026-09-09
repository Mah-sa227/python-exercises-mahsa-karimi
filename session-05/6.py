matn=input('Enter a text:').lower().split()

p=['hack','fraud','scam','password','atack']


for i in p:
   
    count=matn.count(i)
    
    if count>1:
        print(i,':', count)