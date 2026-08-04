print("Salam be foroshgah fanavari khosh amadid")
answer=input("aya mikhahid mahsooli ezafe konid???")

answerrr=answer.lower().strip()

product=['atr','skin product','arayeshi','lebas']

if answerrr=='yes':
    p=input('esme mahsool ro begoo :')
    product.append(p)
    print('ezafe shod :',product)

elif answerrr=='no':
    print('mamnoon khedmat az mast kolish vas mas :D ')
else:
    print('shoma faqat bayad ba yes/no javab bedi')