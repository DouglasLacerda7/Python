brt = float(input("Insira o salário bruto: "))

if brt<= 2121:
    print("Imposto não será pago")

elif brt <= 2628.65:
    descontado = brt * 0.075
    brt_descontado = brt - descontado
    print("O salário liquido é:", brt_descontado, "Parte de 7,5%")

elif brt <= 5137.05:
    descontado = brt * 0.15
    brt_descontado = brt - descontado
    print("O salário liquido é:", brt_descontado, "Parte de 22,5%")

elif brt <= 4664.68:
    descontado = brt * 0.075
    brt_descontado = brt - descontado
    print("O salário liquido é:", brt_descontado, "Parte de 7,5%")
    
else:
    descontado = brt * 0.275
    brt_descontado = brt - descontado
    print("O salário liquido é:", brt_descontado, "Parte de 27.5%")