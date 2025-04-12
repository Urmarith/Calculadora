print("Olá! Por favor, insira seu nome para melhor experiencia.")
nome = input("Nome: ")
print("")
print("Olá", nome, "Bem vindo a sua calculadora! O que deseja calcular hoje?")
print("")
print("1-Formula de bhaskara | 2-Probabilidade | 3-Somar | 4-Tabuada | 5- Calcular média de notas | 6- Calcular média de idade")
escolha = int(input("Insira sua escolha: "))

if escolha==1:
    print("Vamos resolver Bhaskara!")
    a = float(input("Insira o valor de A: "))
    b = float(input("Insira o valor de B: "))
    c = float(input("Insira o valor de C: "))

    delta = b**2-4*a*c

    if delta < 0:
      print ("Não existem raizes reais.")
    else:
      x1 = (-b + delta**0.5)/ (2*a)
      x2 = (-b - delta**0.5)/ (2*a)
      print("Delta é igual a:", delta)
      print("x1 é igual a:", x1)
      print("x2 é igual a:", x2)
      
elif escolha==2:
    print("Vamos resolver probabilidade!")
          
    p = float(input("Insira a probabilidade em decimal (ex.: 30% -> 0.3): "))
    n = int(input("Insira o valor de N: "))
    k = int(input("Insira o valor de K: "))
    
    import math
    
    fden = math.factorial(n)
    fdek = math.factorial(k)
    nek = (n-k)
    fdenek = math.factorial(nek)
    fdenekvezesk = fdek*fdenek
    
    c = fden/fdenekvezesk
    
    formula = (c*(p**k)*(1-p)**nek)*100
    
    print(f"A probabilidade de tal fato ocorrer é de: {formula:.2f}%.")
    
elif escolha==3:
    print("Vamos somar!")
    
    somador = 0
    contador = 0
    n = int(input("Quantos números deseja somar: "))
    
    while contador<n:
        somador += int(input("Digite um número: "))
        contador += 1
    print("A soma dos", n,"números é de:", somador)
    
elif escolha==4:
    print("Vamos calcular uma tabuada!")
    
    numero = int(input("Insira qual tabuada: "))
    
    for contador in range(1,11,1):
        print(numero,"x",contador, " = ", numero*contador)
    
elif escolha==5:
    print("Vamos calcular a média das suas notas!")
    
    from datetime import datetime
    
    nota1 = float(input("A média é feita com quatro notas. Insira sua primeira nota (Apenas valores numéricos): "))
    nota2 = float(input("Ótimo! Insira sua segunda  nota (Apenas valores numéricos): "))
    nota3 = float(input("Ótimo! Insira sua terceira nota (Apenas valores numéricos): "))
    nota4 = float(input("Ótimo! Insira sua última nota (Apenas valores numéricos): "))
    
    media = (nota1 + nota2 + nota3 + nota4) / 4
    
    print(f"Que legal! Sua média foi de: {media:.2f}") #{media:.2f}
    
elif escolha==6:
    print("Vamos calcular sua idade!")
    
    ano_nascimento = int(input("Ótimo! Vamos calcular sua idade! Insira sua data de nascimento (Ex.: 2005): "))
    ano_atual = datetime.now().year
    idade = ano_atual-ano_nascimento
    print(f"Que maneiro! Você tem {idade} anos de idade!")