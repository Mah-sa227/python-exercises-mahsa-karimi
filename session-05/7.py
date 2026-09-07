word = input(' enter : ')
old_w = ''

count= 0
all_count = []
all_character = []

for i in range(0,len(word)):
    
    if old_w == word[i]:
        count +=1
        
        if i == len(word)-1:
            all_count.append(count+1)
            all_character.append(old_w)
        
    else:
        
        all_count.append(count+1)
        all_character.append(old_w)
        count = 0
    old_w=word[i]   

    
new_list=[]
for i in range(1,len(all_count)):
    
    new = all_character[i] + str(all_count[i])
    new_list.append(new)
final = ''.join(new_list)

print(final)        

