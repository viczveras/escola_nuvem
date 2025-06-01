

def calculadora():
  
    print("=== CALCULADORA ===")
    print("Operações válidas: + (adição), - (subtração), * (multiplicação), / (divisão)")
    
    while True:
        try:
            
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            
            operacao = input("Digite a operação (+, -, *, /): ").strip()

            if operacao not in ['+', '-', '*', '/']:
                print("Erro: Operação inválida! Use apenas +, -, * ou /")
                continue
            
            
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida!")
                    continue
                resultado = num1 / num2
            
            # Exibe o resultado e encerra
            print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
            break
            
        except ValueError:
            print("Erro: Entrada inválida! Digite apenas números.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

def registro_notas():

    print("\n=== REGISTRO DE NOTAS ===")
    print("Digite as notas dos alunos (0 a 10) ou 'fim' para encerrar.")
    
    notas = []
    
    while True:
        entrada = input("Digite uma nota: ").strip().lower()
        
        if entrada == 'fim':
            break
        
        try:
            nota = float(entrada)
            
            
            if 0 <= nota <= 10:
                notas.append(nota)
                print(f"Nota {nota} registrada com sucesso!")
            else:
                print("Erro: Nota inválida! Digite uma nota entre 0 e 10.")
                
        except ValueError:
            print("Erro: Entrada inválida! Digite um número ou 'fim'.")
    
    
    if notas:
        media = sum(notas) / len(notas)
        print(f"\nTotal de notas registradas: {len(notas)}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("\nNenhuma nota foi registrada.")

def verificador_senha():

    print("\n=== VERIFICADOR DE SENHA FORTE ===")
    print("Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número.")
    print("Digite 'sair' para encerrar.")
    
    while True:
        senha = input("Digite uma senha: ").strip()
        
        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break
        
 
        if len(senha) < 8:
            print("Senha fraca: deve ter pelo menos 8 caracteres.")
            continue
        
   
        tem_numero = any(char.isdigit() for char in senha)
        if not tem_numero:
            print("Senha fraca: deve conter pelo menos um número.")
            continue
        
        print("Senha forte! Critérios atendidos.")
        break

def contador_pares_impares():
   
    print("\n=== CONTADOR DE PARES E ÍMPARES ===")
    print("Digite números inteiros ou 'fim' para encerrar.")
    
    pares = 0
    impares = 0
    
    while True:
        entrada = input("Digite um número inteiro: ").strip().lower()
        
        if entrada == 'fim':
            break
        
        try:
            numero = int(entrada)
            
            if numero % 2 == 0:
                print(f"{numero} é par.")
                pares += 1
            else:
                print(f"{numero} é ímpar.")
                impares += 1
                
        except ValueError:
            print("Erro: Entrada inválida! Digite um número inteiro ou 'fim'.")
    

    print(f"\nResumo:")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")
    print(f"Total de números válidos: {pares + impares}")

def main():
 
    print("Escolha qual programa executar:")
    print("1. Calculadora")
    print("2. Registro de Notas")
    print("3. Verificador de Senha")
    print("4. Contador Pares/Ímpares")
    print("5. Executar todos")
    
    try:
        escolha = int(input("Digite sua escolha (1-5): "))
        
        if escolha == 1:
            calculadora()
        elif escolha == 2:
            registro_notas()
        elif escolha == 3:
            verificador_senha()
        elif escolha == 4:
            contador_pares_impares()
        elif escolha == 5:
            calculadora()
            registro_notas()
            verificador_senha()
            contador_pares_impares()
        else:
            print("Opção inválida!")
            
    except ValueError:
        print("Erro: Digite um número válido!")

if __name__ == "__main__":
    main()