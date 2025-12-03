# -------------------------------------------
# MINI PROJETO DE CADASTRO DE PRODUTOS
# -------------------------------------------

# Lista onde todos os produtos serão armazenados
produtos = []  


# Estrutura de repetição para cadastrar vários produtos
while True:
    print("\n Cadastro de Produto ")

    # Entrada de dados do usuário
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade em estoque: "))

    # Criação do dicionário com os dados do produto
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    # Adiciona o dicionário na lista de produtos
    produtos.append(produto)

    print("\nProduto cadastrado com sucesso!")

    # Pergunta se o usuário quer continuar cadastrando
    opcao = input("Deseja cadastrar outro produto? (s/n): ").lower()
    
    # Condição para encerrar o loop
    if opcao != "s":
        break


#
# RELATÓRIO FINAL
#
print("\n PRODUTOS CADASTRADOS ")

# Estrutura de repetição para mostrar todos os produtos cadastrados
for p in produtos:
    print(f"- {p['nome']} | Preço: R${p['preco']} | Qtd: {p['quantidade']}")


print("\n ANÁLISE DO ESTOQUE DOS PRODUTOS ")

# Estrutura condicional para analisar cada produto
for p in produtos:
    if p["quantidade"] == 0:
        print(f"O produto '{p['nome']}' está SEM estoque!")
    elif p["quantidade"] < 5:
        print(f"O produto '{p['nome']}' está com estoque BAIXO.")
    else:
        print(f"O produto '{p['nome']}' possui estoque suficiente.")
