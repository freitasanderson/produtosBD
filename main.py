import mysql.connector
from tkinter import * 
from tkinter import messagebox


produtos=[]   

#conexão com banco de dados

con = mysql.connector.connect(host='localhost',database='db_produtos',user='root',password='andex301')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)

#Produto
class Produto:
    def sair():#6 - Sair
        con.commit()
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")
        exit()

    def leituraDosDados(produto,descricao,quantidade):
        produto.descricao = str(descricao.get())
        produto.quantidade = int(quantidade.get())

        if produto.descricao and produto.quantidade:
            messagebox.showinfo(title='Inserção de Produto', message=f'Produto {produto.descricao} adicionado com sucesso.')
            print(f'Inserido: {produto.descricao}-{produto.quantidade} unidades.')
            sql = "INSERT INTO produto (descricao, quantidade) VALUES (%s, %s)"
            values = (produto.descricao, produto.quantidade)
            cursor.execute(sql, values)
            con.commit()
            produtos.append(produto)
        else:
            messagebox.showwarning(title='Inserção de Produto', message=f'Erro, tente novamente.')
    def mostraDados():
        janelaMostraDados = Tk()
        janelaMostraDados.geometry('400x500')
        janelaMostraDados.title ("Estoque de Produto")
        texto = Label(janelaMostraDados, text=f'ID')
        texto.grid(column=0, row=0, padx=20, pady=10)
        texto = Label(janelaMostraDados, text=f'Produto')
        texto.grid(column=1, row=0, padx=20, pady=10)
        texto = Label(janelaMostraDados, text=f'Quantidade')
        texto.grid(column=2, row=0, padx=20, pady=10)
        i=0
        for p in produtos:
            i+=1
            texto = Label(janelaMostraDados, text=f'{i-1}')
            texto.grid(column=0, row=i, padx=0, pady=10)
            texto = Label(janelaMostraDados, text=f'{p.descricao}')
            texto.grid(column=1, row=i, padx=0, pady=10)
            texto = Label(janelaMostraDados, text=f'{p.quantidade}')
            texto.grid(column=2, row=i, padx=0, pady=10)
            
        botao = Button(janelaMostraDados, text="Fechar", bg='orange', command= lambda:[janelaMostraDados.destroy(), Menu()])
        botao.grid(column=1, row=i+2, padx=30, pady=10)

    def atualizaQuantidade(descricao,quantidade,op):
        prodDesc = str(descricao.get())
        prodQt = int(quantidade.get())

        for p in produtos:
            if p.descricao == prodDesc:
                if op == 'Adicionar':
                    if prodQt > 0:
                        p.quantidade += prodQt
                        messagebox.showinfo(title='Atualizar Quantidade de Produto', message=f'Quantidade do Produto {p.descricao} atualizado com sucesso.')
                    else:
                        messagebox.showinfo(title='Atualizar Quantidade de Produto', message=f'Quantidade do Produto {p.descricao} não foi atualizada, foi inserido quantidade incorreta.')
                else:
                    if p.quantidade >= prodQt:
                        p.quantidade -= prodQt
                        messagebox.showinfo(title='Atualizar Quantidade de Produto', message=f'Quantidade do Produto {p.descricao} atualizado com sucesso.')
                    else:
                        messagebox.showwarning(title='Atualizar Quantidade de Produto', message=f'Quantidade não permitida. Somente {p.quantidade} unidades de {p.descricao} disponíveis.')
    
    def retirarProduto(descricao):
        desc = str(descricao.get())
        i=0
        for p in produtos:
            if p.descricao == desc:
                produtos.pop(i)
            i+=1
            
    def __init__(self):#Construtor Vazio
        self.descricao = ''
        self.quantidade = ''

        return


#Janelas e Menus
class Menu:
    def __init__(self):
        janela = Tk()
        janela.geometry('400x400')
        janela.title("Questão 2")
        texto = Label(janela, text="Sistema de Gerenciamento de Produtos")
        texto.grid(column=0, row=0, padx=20, pady=10)

        botao = Button(janela, text="1- Incluir Novo Produto", command= lambda:[janela.destroy(), self.incluirProduto()])
        botao.grid(column=0, row=1, padx=100, pady=10)
        if produtos:
            botao = Button(janela, text="2- Listar Todos os Produtos", command= lambda:[janela.destroy(), Produto.mostraDados()])
            botao.grid(column=0, row=2, padx=10, pady=10)
            botao = Button(janela, text="3- Adicionar ao Estoque", command= lambda:[janela.destroy(), self.adicionarQT()])
            botao.grid(column=0, row=3, padx=10, pady=10)
            botao = Button(janela, text="4- Retirar do Estoque", command= lambda:[janela.destroy(), self.removerQT()])
            botao.grid(column=0, row=4, padx=10, pady=10)
            botao = Button(janela, text="5- Excluir Produto", command= lambda:[janela.destroy(), self.removerProduto()])
            botao.grid(column=0, row=5, padx=10, pady=10)
            botao = Button(janela, text="6- Sair", bg='orange', command=Produto.sair)
            botao.grid(column=0, row=6, padx=10, pady=10)

        janela.mainloop()

    def removerProduto(self):
        janelaRemoverProd = Tk()
        janelaRemoverProd.geometry('400x180')
        janelaRemoverProd.title("Questão 2 - Remover Produto do Estoque ")

        texto = Label(janelaRemoverProd, text="Selecione o Produto para remover do estoque.")
        texto.grid(column=0, row=0, padx=20, pady=5)
        prods = StringVar(janelaRemoverProd)
        tprod=[]
        for p in produtos:
            tprod.append(p.descricao)
        prods.set(tprod[0]) # default value
        prod = OptionMenu(janelaRemoverProd, prods, *tprod)
        prod.grid(column=0, row=1, padx=10, pady=0)


        botaoEnviar = Button(janelaRemoverProd, text="Enviar", bg="green", command= lambda: [Produto.retirarProduto(prods), 
            janelaRemoverProd.destroy(), Menu()])
        botaoEnviar.grid(column=0, row=4, padx=10, pady=10)

    def adicionarQT(self):
        janelaAdicionarQT = Tk()
        janelaAdicionarQT.geometry('400x180')
        janelaAdicionarQT.title("Questão 2 - Atualizar Produto ")

        texto = Label(janelaAdicionarQT, text="Selecione o Produto para atualizar a quantidade")
        texto.grid(column=0, row=0, padx=20, pady=5)
        prods = StringVar(janelaAdicionarQT)
        tprod=[]
        for p in produtos:
            tprod.append(p.descricao)
        prods.set(tprod[0]) # default value
        prod = OptionMenu(janelaAdicionarQT, prods, *tprod)
        prod.grid(column=0, row=1, padx=10, pady=0)

        texto = Label(janelaAdicionarQT, text="Insira a quantidade para adicionar")
        texto.grid(column=0, row=2, padx=20, pady=0)
        quantidade = Entry(janelaAdicionarQT, width=10)
        quantidade.grid(column=0, row=3, padx=10, pady=0)

        botaoEnviar = Button(janelaAdicionarQT, text="Enviar", bg="green", command= lambda: [Produto.atualizaQuantidade(prods, quantidade,'Adicionar'), 
            janelaAdicionarQT.destroy(), Menu()])
        botaoEnviar.grid(column=0, row=4, padx=10, pady=10)

    def removerQT(self):
        janelaRemoverQT = Tk()
        janelaRemoverQT.geometry('400x180')
        janelaRemoverQT.title("Questão 2 - Atualizar Produto ")

        texto = Label(janelaRemoverQT, text="Selecione o Produto para atualizar a quantidade")
        texto.grid(column=0, row=0, padx=20, pady=5)
        prods = StringVar(janelaRemoverQT)
        tprod=[]
        for p in produtos:
            tprod.append(p.descricao)
        prods.set(tprod[0]) # default value
        prod = OptionMenu(janelaRemoverQT, prods, *tprod)
        prod.grid(column=0, row=1, padx=10, pady=0)

        texto = Label(janelaRemoverQT, text="Insira a quantidade para adicionar")
        texto.grid(column=0, row=2, padx=20, pady=0)
        quantidade = Entry(janelaRemoverQT, width=10)
        quantidade.grid(column=0, row=3, padx=10, pady=0)

        botaoEnviar = Button(janelaRemoverQT, text="Enviar", bg="green", command= lambda: [Produto.atualizaQuantidade(prods, quantidade,'Remover'), 
            janelaRemoverQT.destroy(), Menu()])
        botaoEnviar.grid(column=0, row=4, padx=10, pady=10)

    def incluirProduto(self):
        produto = Produto()
        janelaIncluir = Tk()
        janelaIncluir.geometry('400x180')
        janelaIncluir.title("Questão 2 - Incluir Novo Produto ")

        texto = Label(janelaIncluir, text="Insira a descrição do produto")
        texto.grid(column=0, row=0, padx=20, pady=5)
        descricao = Entry(janelaIncluir, width=45)
        descricao.grid(column=0, row=1, padx=10, pady=0)

        texto = Label(janelaIncluir, text="Insira a quantidade inicial")
        texto.grid(column=0, row=2, padx=20, pady=0)
        quantidade = Entry(janelaIncluir, width=10)
        quantidade.grid(column=0, row=3, padx=10, pady=0)

        botaoEnviar = Button(janelaIncluir, text="Enviar", bg="green", command= lambda: [Produto.leituraDosDados(produto, descricao,quantidade), 
            janelaIncluir.destroy(), Menu()])
        botaoEnviar.grid(column=0, row=4, padx=10, pady=10)
        
        janelaIncluir.mainloop()


if con.is_connected():
    
    Menu()