word = input('enter  : \n')
total_char = 0
alpha = 0
lower = 0
upper = 0
digit = 0
space = 0
for i in word :
    total_char += 1
    if i.isalpha():
        alpha += 1
        if i.islower() :
            lower += 1
        else :
            upper += 1
    elif i.isdigit() :
        digit += 1
    elif i.isspace() :
        space += 1

t = {}
num = 0
for i in word :
    if i in t and i != ' ':
        t[i] += 1
    else :
        t[i] = 1
for i, j in t.items() :
    if j > num :
        num = j
        most_rep_char = i

my_list = word.split(' ')
d = {}
num_word = 0
for i in my_list :
    if i in d :
        d[i] += 1
    else :
        d[i] = 1
for i, j in d.items() :
    if j > num_word :
        num_rep_word = j
        most_rep_word = i
        
max_len = 0
min_len = 999999
for i in d.keys() :
    if len(i) > max_len :
        max_len = len(i)
        long_word = i
    if len(i) < min_len and i != ' ' :
        min_len = len(i)
        short_word = i
        
print ('Total characters :',total_char,'\n'
       'Total letters :',alpha,'\n' 
       'Total digits :',digit,'\n'
       'Total spaces :',space,'\n'
       'Total uppercase :',upper,'\n'
       'Total lowercase :',lower,'\n'
       'Longest word :',long_word,'\n'
       'Shortest word :',short_word,'\n'
       'Most repeated character :',most_rep_char,'\n'
       'Most repeated word :',most_rep_word)