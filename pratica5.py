

import re
from datetime import datetime

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):

    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

def verificar_palindromo(texto):

    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

def calcular_preco_com_desconto():

    print("=== CALCULADORA DE DESCONTO ===")
    
    try:
        
        preco_original = float(input("Digite o preço do produto: R$ "))
        
        
        if preco_original < 0:
            print("Erro: O preço não pode ser negativo!")
            return
        
        
        percentual_desconto = float(input("Digite o percentual de desconto (%): "))
        
        
        if percentual_desconto < 0 or percentual_desconto > 100:
            print("Erro: O percentual de desconto deve estar entre 0 e 100!")
            return
        
       
        valor_desconto = preco_original * (percentual_desconto / 100)
        
       
        preco_final = preco_original - valor_desconto
        
        
        print(f"\nPreço original: R$ {preco_original:.2f}")
        print(f"Desconto ({percentual_desconto}%): R$ {valor_desconto:.2f}")
        print(f"Preço final: R$ {preco_final:.2f}")
        
    except ValueError:
        print("Erro: Digite valores numéricos válidos!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def calcular_idade_em_dias(ano_nascimento):
  
    ano_atual = datetime.now().year
    
  
    idade_anos = ano_atual - ano_nascimento
 
    idade_dias = idade_anos * 365
    
    return idade_dias

def menu_gorjeta():
   
    print("\n=== CALCULADORA DE GORJETA ===")
    
    try:
        valor_conta = float(input("Digite o valor total da conta: R$ "))
        if valor_conta < 0:
            print("Erro: O valor da conta não pode ser negativo!")
            return
            
        porcentagem = float(input("Digite a porcentagem de gorjeta (%): "))
        if porcentagem < 0:
            print("Erro: A porcentagem não pode ser negativa!")
            return
        
        gorjeta = calcular_gorjeta(valor_conta, porcentagem)
        total = valor_conta + gorjeta
        
        print(f"\nValor da conta: R$ {valor_conta:.2f}")
        print(f"Gorjeta ({porcentagem}%): R$ {gorjeta:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")
        
    except ValueError:
        print("Erro: Digite valores numéricos válidos!")

def menu_palindromo():
    
    print("\n=== VERIFICADOR DE PALÍNDROMO ===")
    
    texto = input("Digite uma palavra ou frase: ")
    resultado = verificar_palindromo(texto)
    print(f"'{texto}' é um palíndromo? {resultado}")

def menu_idade_dias():
  
    print("\n=== CALCULADORA DE IDADE EM DIAS ===")
    
    try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        ano_atual = datetime.now().year
        
        if ano_nascimento > ano_atual:
            print("Erro: O ano de nascimento não pode ser no futuro!")
            return
        
        if ano_nascimento < 1900:
            print("Erro: Digite um ano válido (a partir de 1900)!")
            return
        
        idade_dias = calcular_idade_em_dias(ano_nascimento)
        idade_anos = ano_atual - ano_nascimento
        
        print(f"\nIdade aproximada: {idade_anos} anos")
        print(f"Idade em dias: {idade_dias} dias")
        
    except ValueError:
        print("Erro: Digite um ano válido!")

def main():
    
    print("=== PROGRAMA PRÁTICA 5 ===")
    print("Escolha uma opção:")
    print("1. Calculadora de Gorjeta")
    print("2. Verificador de Palíndromo")
    print("3. Calculadora de Desconto")
    print("4. Calculadora de Idade em Dias")
    print("5. Executar todos")
    
    try:
        escolha = int(input("Digite sua escolha (1-5): "))
        
        if escolha == 1:
            menu_gorjeta()
        elif escolha == 2:
            menu_palindromo()
        elif escolha == 3:
            calcular_preco_com_desconto()
        elif escolha == 4:
            menu_idade_dias()
        elif escolha == 5:
            menu_gorjeta()
            menu_palindromo()
            calcular_preco_com_desconto()
            menu_idade_dias()
        else:
            print("Opção inválida! Escolha entre 1 e 5.")
            
    except ValueError:
        print("Erro: Digite um número válido!")

if __name__ == "__main__":
    main()