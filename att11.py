def cv(preco, ccp):
    if ccp==1:
        return preco*0.9
    elif ccp==2: 
        return preco*0.85
    elif ccp==3:
        return preco
    elif ccp==4:
        return preco*1.1
    else: 
        return"Condição de pagamento invalidado"
    
preco=float(input("Insira o preço do produto"))
ccp=int(input("Insira a condição: 1 , 2 , 3 , 4"))

valor_a_pagar=cv(preco, ccp)

print("Valor a ser pago", valor_a_pagar)