word = input(' enter :  ')

repeat = []

for i in word:
    if i not in repeat:
        repeat +=i

        
repeat=''.join(repeat)
print(repeat)
