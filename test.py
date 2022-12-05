import mysql.connector

con = mysql.connector.connect(host='localhost',database='db_produtos',user='root',password='andex301')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)

def sair():#6 - Sair
    con.commit()
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")
    exit()


if con.is_connected():

    sql = "SELECT * FROM produto"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(f'Conteudo: {rs}')
    for r in rs:
        print(f'Tamanho: {len(r)}')
        
        print(f'Nome do Produto:{r[1]} Quantidade:{r[2]}')