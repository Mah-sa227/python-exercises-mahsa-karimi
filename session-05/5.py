s = input(' enter : ')
sentence=s.split()
toolanitarin = []

for i in sentence:
    
    temp= sentence.count(i)
    
    if len(i)> len(toolanitarin):
        
        toolani = i
        
print(toolanitarin , ':' , len(toolanitarin))        