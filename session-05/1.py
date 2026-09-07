print('رمز باید حداقل 8 کاراکتر داشته باشد \nحداقل یک حرف بزرگ و یک حرف کوچک \nحداقل یک عدد و یک کاراکتر خاص مثل @ # $ % ')

password = input('enter pass :')
    
special=['@','#','$','%']

if not any(i.islower() for i in password):
   
        print('lowercase yadet raft')
        
if not any(i.isupper() for i in password ):
        
        print('uppercase yadet raft')
        
if not any(i.isdigit() for i in password ):
        
        print(' adad yadet raft ')
        
if len(password)<8:
        
        print(' at least 8 charachter ')

if not any( i in special for i in password):
        
         print(' alaeme khas yadet raft ')
         
else:
    print('password is valid.... ')        