j = input(' ye chizi begoo : ')

jomle=j.lower().split()

repeat = []

for i in jomle:
    
    s = jomle.count(i)
    
    if s > 0 :
        
        repeat = i
      
print(repeat, ':' , s)       