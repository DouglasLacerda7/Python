altura = float(input("Insira sua altura"))
sexo=input("Insira seu sexo. M ou F")
if sexo == 'M' : 
    peso_ideal=(72.7 * altura)-58
elif sexo== 'F':
    peso_ideal=(62.1 * altura)-44.7
else : 
    print("Sexo não reconhecido. Insira F ou M")
print(peso_ideal)