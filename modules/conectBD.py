import mysql.connector

#conexão com banco de dados
def Conectar():
    con = mysql.connector.connect(host='teste.c0sjio5nc9zh.sa-east-1.rds.amazonaws.com',database='bd_produtos',user='root',password='andex301')
    return con

    