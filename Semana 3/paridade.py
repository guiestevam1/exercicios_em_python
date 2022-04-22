div=2
cont=0
resto=1
while resto!=0:
    if numero<2:
        resto=0
        break
    resto=numero%div
    cont+=1
    div=(2*cont)+1
    if div==numero:
        break
if resto==0 and numero!=2:
    print("Nao e primo")
else:
    print("E numero primo")
