import modules.conectBD as Conect

#Conectar com o banco de dados:
con = Conect.Conectar()

#Se conectado:
if con.is_connected():
    print(f'Conectado: {con.is_connected()}')
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)

#Antes de tentar inserir no banco de dados, procura se o produto ja existe no banco de dados
def VerificaProduto(produto):
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)
    rs = cursor.fetchall()

    for r in rs:
        if produto == r[1]:
            return False
    return True


def VerificaProdutoExcluir(produto):
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)
    rs = cursor.fetchall()

    for r in rs:
        if produto == r[1]:
        
            return False
    return True

def VerificaQuantidade(produto,quantidade):
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)
    rs = cursor.fetchall()

    for r in rs:
        if produto == r[1]:
            if quantidade > r[2]:
                return False
            else:    
                return True
#Menu principal que lista as opções, chama funções e executa comandos SQL.
def Options():
    print(f'\n1- Incluir Novo Produto')
    print(f'2- Listar Todos os Produtos')
    print(f'3- Adicionar ao Estoque')
    print(f'4- Retirar do Estoque')
    print(f'5- Excluir Produto')
    print(f'6- Sair\n')

    #Pega a opção do usuário
    op = int(input())

    #Estrutura semelhante ao Switch Case da Linguagem C
    match op:

        #Inserir Produto
        case 1:
            prod = input('\nDigite o Nome do Produto: ')
            quant = int(input('Digite a Quantidade: '))

            if VerificaProduto(prod):
                sql = "INSERT INTO produtos (descricao, quantidade) VALUES (%s, %s)"
                values = (prod, quant)
                cursor.execute(sql, values)
                con.commit()
                print(f'O Produto {prod} foi inserido com sucesso.')
                return 
            else:
               print(f'ERROR: Produto {prod} já existe, se quiser, você pode alterar a quantidade.')
               return 
        #Listar todos os produtos
        case 2:
            sql = "SELECT * FROM produtos"
            cursor.execute(sql)
            rs = cursor.fetchall()

            print(f'\nTemos {len(rs)} produto(s):\n')
            for r in rs:
                
                print(f'\tProduto: {r[1]} Quantidade: {r[2]}')
            return

        #Adicionar ao estoque de produto existente
        case 3:
            sql = "SELECT * FROM produtos"
            cursor.execute(sql)
            rs = cursor.fetchall()

            print(f'\nTemos {len(rs)} produto(s):\n')
            for r in rs:
                
                print(f'\tProduto: {r[1]} Quantidade: {r[2]}')
            
            prod = input('\nDigite o produto que deseja aumentar a quantidade:')
            quant = int(input('Digite a Quantidade: '))

            #Se adicionar quantidade negativa o cabloco vai cair aqui.    
            while quant <= 0:
                print('Digite um valor maior que 0.')
                quant = int(input('Digite a Quantidade: '))

            if VerificaProduto(prod):
               print(f'ERROR: Produto {prod} não existe.')
            
            else:
                sql = (f'UPDATE produtos SET quantidade = quantidade + {quant} where descricao = "{prod}"')
                cursor.execute(sql)
                con.commit()
        
        #Retirar do estoque de produto existente
        case 4:
            sql = "SELECT * FROM produtos"
            cursor.execute(sql)
            rs = cursor.fetchall()

            print(f'\nTemos {len(rs)} produto(s):\n')
            for r in rs:
                
                print(f'\tProduto: {r[1]} Quantidade: {r[2]}')
            
            prod = input('\nDigite o produto que deseja diminuir a quantidade:')
            quant = int(input('Digite a Quantidade: '))

            #Se adicionar quantidade negativa o cabloco vai cair aqui.    
            while quant <= 0:
                print('Digite um valor maior que 0.')
                quant = int(input('Digite a Quantidade: '))

            if VerificaQuantidade(prod,quant):
                sql = (f'UPDATE produtos SET quantidade = quantidade - {quant} where descricao = "{prod}"')
                cursor.execute(sql)
                con.commit()
            
            else:
                print(f'ERROR: Quantidade do Produto {prod} excedida.')


        #Excluir Produto
        case 5:
            sql = "SELECT * FROM produtos"
            cursor.execute(sql)
            rs = cursor.fetchall()

            print(f'\nTemos {len(rs)} produto(s):\n')
            for r in rs:
                
                print(f'\tProduto: {r[1]} Quantidade: {r[2]}')
            
            prod = input('\nDigite o produto que deseja excluir:')

            if VerificaProdutoExcluir(prod):
               print(f'ERROR: Produto {prod} não existe.')
            else:
                sql = (f'DELETE FROM produtos Where descricao = "{prod}"')
                cursor.execute(sql)
                con.commit()

        case 6:
            con.commit()
            cursor.close()
            con.close()
            print("Conexão ao MySQL foi encerrada")
            exit()