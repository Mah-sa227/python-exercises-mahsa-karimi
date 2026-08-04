h=int(input('ارتفاع را وارد کنید :'))
Max=0
for i in range(1,10):
    if h<Max:
        print('قبلا ثبت شده است')
        h=int(input('ارتفاع را وارد کن :'))
    else:
        Max=h
    print('رکورد تازه ثبت شد')
    h=int(input('ارتفاع را وارد کن :'))
    
Max=h
print('بیشترین پرش تااین لحظه :', Max,'metr') 
