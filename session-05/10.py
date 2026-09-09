jomle1 = input(' enter first sentence : ').lower().split()

jomle2 = input(' enter second : ').lower().split()

moshtarak = []

for i in jomle1:
   
    if i in jomle2:
        
        moshtarak.append(i)
        
        
print(moshtarak)