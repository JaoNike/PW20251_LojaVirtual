from data.database import obter_conexao
from sql.produto_sql import *
from models.produto import Produto

def criar_tabela_produtos() -> bool:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(CREATE_TABLE_PRODUTO)
        return (cursor.rowcount >= 0)
        

def inserir_produto(produto: Produto) -> Produto:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(INSERT_PRODUTO, 
            (produto.nome, produto.descricao, produto.preco, produto.estoque, produto.imagem))
        produto.id = cursor.lastrowid
        return produto

def atualizar_produto(produto: Produto) -> bool:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(UPDATE_PRODUTO, 
            (produto.nome, produto.descricao, produto.preco, produto.estoque, produto.imagem, produto.id))
        return (cursor.rowcount > 0)

def excluir_produto(id: int) -> bool:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(DELETE_PRODUTO, (id,))
        return (cursor.rowcount > 0)

def obter_produto_por_id(id: int) -> Produto:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(GET_PRODUTO_BY_ID, (id,))
        resultado = cursor.fetchone()
        conexao.close()
        if resultado:
            return Produto(
                id=resultado[0],
                nome=resultado[1],
                descricao=resultado[2],
                preco=resultado[3],
                estoque=resultado[4],
                imagem=resultado[5]
            )
        return None

def obter_produtos_por_pagina(limite: int, offset: int) -> list[Produto]:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(GET_PRODUTOS_BY_PAGE, (limite, offset))
        resultados = cursor.fetchall()
        conexao.close()
        return [Produto(
            id=resultado[0],
            nome=resultado[1],
            descricao=resultado[2],
            preco=resultado[3],
            estoque=resultado[4],
            imagem=resultado[5]
        ) for resultado in resultados]