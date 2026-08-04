a=input('enter a word :')
b=int(len(a))
if b%2==0:
    nesf=b//2
    print(a[0:nesf])
else:
    b%2!=0
    nesf=b//2
    print(a[nesf:])
    