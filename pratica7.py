import csv
import json
import statistics

def calcular_media_desvio_log(filepath):
    try:
        with open(filepath, 'r') as file:
            tempos = []
            for linha in file:
                try:
                    tempo = float(linha.strip())
                    tempos.append(tempo)
                except ValueError:
                    pass
            if tempos:
                media = statistics.mean(tempos)
                desvio = statistics.stdev(tempos)
                print(f"Média: {media:.2f}, Desvio padrão: {desvio:.2f}")
            else:
                print("Nenhum dado válido encontrado no arquivo.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def escrever_dados_csv(filepath, dados):
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Idade", "Cidade"])
        writer.writerows(dados)
    print(f"Dados escritos no arquivo {filepath} com sucesso.")

def ler_dados_csv(filepath):
    try:
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            for linha in reader:
                print(linha)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def ler_escrever_json(filepath, dados=None):
    if dados:
        with open(filepath, 'w') as file:
            json.dump(dados, file, indent=4)
        print(f"Dados escritos no arquivo {filepath} com sucesso.")
    else:
        try:
            with open(filepath, 'r') as file:
                conteudo = json.load(file)
                print(conteudo)
        except FileNotFoundError:
            print("Arquivo não encontrado.")

if __name__ == "__main__":
    print("Escolha uma opção:")
    print("1 - Calcular média e desvio padrão de tempos de execução (log)")
    print("2 - Escrever dados em arquivo CSV")
    print("3 - Ler dados de arquivo CSV")
    print("4 - Ler e escrever dados em arquivo JSON")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        filepath = input("Informe o caminho do arquivo de log: ").strip()
        calcular_media_desvio_log(filepath)
    elif opcao == "2":
        filepath = input("Informe o caminho do arquivo CSV: ").strip()
        dados = [
            ["Alice", 30, "São Paulo"],
            ["Bob", 25, "Rio de Janeiro"],
            ["Carol", 35, "Belo Horizonte"]
        ]
        escrever_dados_csv(filepath, dados)
    elif opcao == "3":
        filepath = input("Informe o caminho do arquivo CSV: ").strip()
        ler_dados_csv(filepath)
    elif opcao == "4":
        filepath = input("Informe o caminho do arquivo JSON: ").strip()
        acao = input("Deseja ler ou escrever dados? (ler/escrever): ").strip().lower()
        if acao == "escrever":
            dados = {
                "nome": "Alice",
                "idade": 30,
                "cidade": "São Paulo"
            }
            ler_escrever_json(filepath, dados)
        elif acao == "ler":
            ler_escrever_json(filepath)
        else:
            print("Ação inválida.")
    else:
        print("Opção inválida.")