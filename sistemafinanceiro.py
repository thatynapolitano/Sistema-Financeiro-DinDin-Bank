import datetime
import csv 

print("-" * 40)
print("Seja bem-vindo ao DinDin Bank. Um Sistema Financeiro para uso pessoal.")
print("-" * 40)


def ler_csv():
    registros_existentes = []
    try:
        with open("registros_financeiros.csv", "r") as arquivo_leitura:

            leitor = csv.DictReader(arquivo_leitura)
            registros_existentes = list(leitor)
    except FileNotFoundError:
        print("Criando aquivo. Arquivo não existente.")

    return registros_existentes


def escrever_csv(registros):
    with open("registros_financeiros.csv", "w") as arquivo:
        if registros:
            escritor = csv.DictWriter(arquivo, fieldnames=lista_registros[0].keys(), lineterminator='\n')
            escritor.writeheader()
            escritor.writerows(registros)

def obter_data_atual():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def receita():
    print("Você selecionou a opção Receita")
    receita_valor = float(input("Digite o valor (R$) da receita: "))
    return {"id": id_atual , "tipo": "receita", "valor": receita_valor, "data": obter_data_atual()}

def despesa():
    despesa_valor = float(input("Digite o valor (R$) da despesa: "))
    return {"id": id_atual, "tipo": "despesa", "valor": -despesa_valor, "data": obter_data_atual()}

calcula_montante = lambda investimento_valor: round(investimento_valor * (1 + 0.02)**30, 2)

def investimento():
    print("Você selecionou a opção Investimento")
    investimento_valor = float(input("Digite o valor (R$) do investimento: "))
    montante = calcula_montante(investimento_valor)
    return {"id": id_atual, "tipo": "investimento", "valor": montante, "data": obter_data_atual()}


def cadastrar_registro(id_atual):
    print("-" * 40)
    print("Você selecionou a Opção de Cadastrar Registro")
    print(f"O ID do registro é: {id_atual}")
    opcoes_registro = {
        1: receita,
        2: despesa,
        3: investimento
    }

    escolha = int(input("Escolha um tipo de registro: \n"
                        "1- Receita \n"
                        "2- Despesa \n"
                        "3- Investimento \n"
                        "4- Retornar \n >>"))
    
    if escolha in opcoes_registro:
        print("-" * 40)
        registro_funcao = opcoes_registro[escolha]
        dicionario_registro = registro_funcao()
        lista_registros.append(dicionario_registro)
        escrever_csv(lista_registros)

def consultar_registro():
    print("-" * 40)
    print("Você selecionou a Opção de Consultar Registro")
    
    opcao = int(input("Consultar registro por: \n"
                      "1- Data \n"
                      "2- Tipo \n"
                      "3- Valor \n"
                      "4- ID \n"
                      "5- Filtrar todos \n"
                      "6- Retornar \n >>")) 

    registros_filtrados = []

    if opcao == 1:
        filtro_data = input("Digite a data do registro para filtrar (AAAA-MM-DD): ")
        try:
            filtro_data = datetime.datetime.strptime(filtro_data, "%Y-%m-%d").strftime("%Y-%m-%d")
            for registro in lista_registros:
                if registro['data'].startswith(filtro_data):
                    registros_filtrados.append(registro)
        except ValueError:
            print("Formato de data inválido. Use AAAA-MM-DD.")
            filtro_data = input("Digite a data do registro para filtrar (AAAA-MM-DD): ")
        
    elif opcao == 2:
        filtro_tipo = input("Digite o tipo do registro para filtrar: ")
        for registro in lista_registros:
            if registro['tipo'].lower() == filtro_tipo.lower():
                registros_filtrados.append(registro)

    elif opcao == 3:
        try:
            filtro_valor = float(input("Digite o valor do registro para filtrar: "))
            for registro in lista_registros:
                if float(registro['valor']) == filtro_valor:
                    registros_filtrados.append(registro)
        except ValueError:
            print("Digite um valor numérico para filtrar por valor.")
            filtro_valor = float(input("Digite o valor do registro para filtrar: "))

    elif opcao == 4: 
        try:
            filtro_valor = int(input("Digite o ID do registro para filtrar: "))
            
            for registro in lista_registros:
                if int(registro['id']) == filtro_valor:
                    registros_filtrados.append(registro)
        except ValueError:
            print("Digite um valor numérico para filtrar por ID.")
            filtro_valor = int(input("Digite o ID do registro para filtrar: "))
            
    elif opcao == 5:
        registros_filtrados = lista_registros
    
    elif opcao == 6:
        return
    
    else:
        print("Opção inválida.")
        return
    
    if not registros_filtrados:
        print("Nenhum registro encontrado.")
    else:
        print("Registros Filtrados:")
        for registro_filtrado in registros_filtrados: 
            print(f"ID: {registro_filtrado['id']}, Tipo: {registro_filtrado['tipo']}, Valor: {registro_filtrado['valor']}, Data: {registro_filtrado['data']}")

def atualizar_registro():
    print("-" * 20)
    print("Você selecionou a Opção de Atualizar Registro")

    try:
        id_atualizar = input("Digite o ID do registro a ser atualizado: ")
        
        for registro in lista_registros:
            if registro['id'] == id_atualizar:
                print("Registro encontrado. Atualize as informações:")
                
                novo_tipo = input(f"Novo tipo (anterior: {registro['tipo']}): ").strip()
                novo_valor = float(input(f"Novo valor (R$) (anterior: {registro['valor']}): "))
                nova_data = obter_data_atual()
                
                if novo_tipo.lower() == "despesa":
                    novo_valor = -abs(novo_valor)
                elif novo_tipo.lower() == "investimento":
                    taxa_de_juros = 0.02 
                    tempo_dias = 30
                    novo_valor = round(novo_valor * (1 + taxa_de_juros)**tempo_dias,2)
                 

                registro['tipo'] = novo_tipo if novo_tipo else registro['tipo']
                registro['valor'] = novo_valor if novo_valor else registro['valor']
                registro['data'] = nova_data if nova_data else registro['data']

                escrever_csv(lista_registros)
                print("Registro atualizado com sucesso.")
                return

    except ValueError:
        print("Digite um valor numérico para o ID ou um valor válido para o novo valor.")


def remover_registro(): 
    print("-" * 40)
    print("Você selecionou a Opção de Remover Registro")
    entrada = input("Insira o ID do registro a ser removido: ")

    for registro in lista_registros:
        if (registro['id'] == entrada): 
            lista_registros.remove(registro)
            print("Registro removido com sucesso.")

            escrever_csv(lista_registros)
            return
    else: 
        print("ID não encontrado. Nenhum registro removido.")
        return

def ler_id():
    if len(lista_registros) > 0:
        ultimo_registro = lista_registros[-1]
        indice = int(ultimo_registro["id"])
        return indice
    else: 
        return 0
    
    

def main():
    global lista_registros
    global id_atual 
    lista_registros = ler_csv ()
    id_atual = ler_id()
    while True:
        try:
            opcao = int(input("Escolha a opção desejada: \n"
                              "1- Cadastrar Registro \n"
                              "2- Consultar Registro \n"
                              "3- Atualizar Registro \n"
                              "4- Remover Registro \n"
                              "5- Sair\n>>"))

            if opcao == 1:
                id_atual += 1
                cadastrar_registro(id_atual)
            elif opcao == 2:
                consultar_registro()
            elif opcao == 3:
                 atualizar_registro()
            elif opcao == 4:
                remover_registro()
            elif opcao == 5:
                print("Programa finalizado")
                break 
            else:
                print("Digite uma opção válida")
                continue
        except ValueError:
            print("Digite uma opção válida. Digite valores inteiros para acessar a opção desejada.")

if __name__ == "__main__":
    main()
