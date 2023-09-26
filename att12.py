nota1= float(input("Insira a primeira nota"))
nota2= float(input("Insira a segunda nota"))
nota3= float(input("Insira a terceira nota"))
me= float(input("Insira a média"))

ma=(nota1+nota2*2+nota3*3+me)/7

if ma>=90: 
    print("A, aprovado")
elif ma>=75 and ma<=90:
    print("B, aprovado")
elif ma>=60 and ma<=75:
    print("C, aprovado")
elif ma>=40 and ma<=60:
    print("D, reprovado")
else:
    print("E, reprovado")

