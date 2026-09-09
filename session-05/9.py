user = input(' enter user :')
password = input(' enter pass :')

print('faqat 3 bar mitoni emtehan koni')



for i in range(1,4):
    
    u = input( ' enter username :')
    p = input(' enter password :')
   
    if u == user and p == password :
        print('Login successful ...')
        break
        
    else:
        remaining = 3 - i
        print('Wrong username or password ')
        print('Atempts remaining:', remaining)