import random
import requests

def gerar_senha_aleatoria():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/"
    tamanho = int(input("Informe a quantidade de caracteres para a senha: "))
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    print(f"Senha gerada: {senha}")

def gerar_perfil_usuario():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        nome = dados['results'][0]['name']['first'] + " " + dados['results'][0]['name']['last']
        email = dados['results'][0]['email']
        pais = dados['results'][0]['location']['country']
        print(f"Nome: {nome}\nEmail: {email}\nPaís: {pais}")
    else:
        print("Erro ao gerar perfil de usuário.")

def consultar_endereco_por_cep():
    cep = input("Informe o CEP: ").strip()
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if "erro" not in dados:
            logradouro = dados.get("logradouro", "Não informado")
            bairro = dados.get("bairro", "Não informado")
            cidade = dados.get("localidade", "Não informado")
            estado = dados.get("uf", "Não informado")
            print(f"Logradouro: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}")
        else:
            print("CEP não encontrado.")
    else:
        print("Erro ao consultar o CEP.")

def consultar_cotacao_moeda():
    moeda = input("Informe o código da moeda (ex: USD, EUR, GBP): ").strip().upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        chave = f"{moeda}BRL"
        if chave in dados:
            cotacao = dados[chave]
            valor_atual = cotacao.get("bid", "Não informado")
            valor_maximo = cotacao.get("high", "Não informado")
            valor_minimo = cotacao.get("low", "Não informado")
            ultima_atualizacao = cotacao.get("create_date", "Não informado")
            print(f"Valor atual: {valor_atual}\nValor máximo: {valor_maximo}\nValor mínimo: {valor_minimo}\nÚltima atualização: {ultima_atualizacao}")
        else:
            print("Moeda não encontrada.")
    else:
        print("Erro ao consultar a cotação.")

if __name__ == "__main__":
    print("Escolha uma opção:")
    print("1 - Gerar senha aleatória")
    print("2 - Gerar perfil de usuário aleatório")
    print("3 - Consultar endereço por CEP")
    print("4 - Consultar cotação de moeda estrangeira")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        gerar_senha_aleatoria()
    elif opcao == "2":
        gerar_perfil_usuario()
    elif opcao == "3":
        consultar_endereco_por_cep()
    elif opcao == "4":
        consultar_cotacao_moeda()
    else:
        print("Opção inválida.")