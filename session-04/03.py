print('رمز باید 8 کاراکتر باشد و چهار کاراکتر اول حروف و مابقی عدد باشد')

while True:
    ramz=input('enter code:')
    
    if ramz[0:4].isalpha() and len(ramz)==8 and ramz[4:].isdigit():
        print('معتبر است')
        break
    else:
        print('نامعتبر')
        continue