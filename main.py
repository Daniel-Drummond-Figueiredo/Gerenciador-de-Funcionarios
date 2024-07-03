print("Bem vindo a empresa de Daniel Drummond Figueiredo")

lista_funcionarios = []
id_global = 4893572

# Cadastrar um funcionário
def cadastrar_funcionario(id):
    print(f"ID do novo funcionário: {id}")
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }
    lista_funcionarios.append(funcionario.copy())

# Consultar funcionários
def consultar_funcionarios():
    while True:
        opcao = int(input("Consultar (1. Todos / 2. Por Id / 3. Por Setor / 4. Retornar): "))
        if opcao == 1:
            for func in lista_funcionarios:
                print(func)
        elif opcao == 2:
            id_consulta = int(input("Digite o ID do funcionário: "))
            encontrado = False
            for func in lista_funcionarios:
                if func['id'] == id_consulta:
                    print(func)
                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não encontrado.")
        elif opcao == 3:
            setor_consulta = input("Digite o setor: ")
            encontrados = [func for func in lista_funcionarios if func['setor'] == setor_consulta]
            if encontrados:
                for func in encontrados:
                    print(func)
            else:
                print("Nenhum funcionário encontrado no setor informado.")
        elif opcao == 4:
            return
        else:
            print("Opção inválida")

# Remover um funcionário
def remover_funcionario():
    while True:
        id_remover = int(input("Digite o ID do funcionário a ser removido: "))
        for func in lista_funcionarios:
            if func['id'] == id_remover:
                lista_funcionarios.remove(func)
                print("Funcionário removido com sucesso.")
                return
        print("ID inválido. Tente novamente.")

# Menu principal
while True:
    opcao = int(input("Escolha uma opção (1. Cadastrar / 2. Consultar / 3. Remover / 4. Encerrar): "))
    if opcao == 1:
        id_global += 1
        cadastrar_funcionario(id_global)
    elif opcao == 2:
        consultar_funcionarios()
    elif opcao == 3:
        remover_funcionario()
    elif opcao == 4:
        break
    else:
        print("Opção inválida")

# Consultas
print("\nConsulta de todos os funcionários:")
consultar_funcionarios()

print("\nConsulta por ID de um dos funcionários:")
consultar_funcionarios()

print("\nConsulta por setor:")
consultar_funcionarios()

print("\nRemoção de um dos funcionários e consulta de todos:")
remover_funcionario()
consultar_funcionarios()