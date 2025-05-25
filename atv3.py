# q 1 
raio = float(input("Digite o valor do raio: "))


pi = 3.14


area = pi * (raio ** 2)


print(f"A={area:.4f}")


# q 2

idade = int(input("Digite sua idade: "))


if idade >= 0 and idade <= 12:
    classificacao = "Criança"
elif idade >= 13 and idade <= 17:
    classificacao = "Adolescente"
elif idade >= 18 and idade <= 59:
    classificacao = "Adulto"
elif idade >= 60:
    classificacao = "Idoso"
else:
    classificacao = "Idade inválida"

print(f"Classificação: {classificacao}")


#q 3  
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)


if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")


#q 4

def converter_temperatura(temp, origem, destino):
    if origem == "F":
        celsius = (temp - 32) * 5/9
    elif origem == "K":
        celsius = temp - 273.15
    else:  # origem == "C"
        celsius = temp
    
    if destino == "F":
        resultado = celsius * 9/5 + 32
    elif destino == "K":
        resultado = celsius + 273.15
    else:  
        resultado = celsius
    
    return resultado


temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C/F/K): ").upper()
destino = input("Digite a unidade de destino (C/F/K): ").upper()


resultado = converter_temperatura(temperatura, origem, destino)

print(f"{temperatura}°{origem} = {resultado:.2f}°{destino}")

# q 5

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")

#  q 6 
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total de vendas: "))


comissao = total_vendas * 0.15


total_receber = salario_fixo + comissao

print(f"TOTAL = R$ {total_receber:.2f}")


# q 7
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))


media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / (2 + 3 + 4 + 1)

print(f"Media: {media:.1f}")


if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:  
    print("Aluno em exame.")
    
   
    nota_exame = float(input("Digite a nota do exame: "))
    print(f"Nota do exame: {nota_exame:.1f}")
    
 
    media_final = (media + nota_exame) / 2
    
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media_final:.1f}")