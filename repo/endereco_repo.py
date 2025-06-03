from data.database import obter_conexao
from sql.endereco_sql import *
from models.endereco import Endereco

def criar_tabela_enderecos() -> bool:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(CREATE_TABLE_ENDERECO)
        return (cursor.rowcount >= 0)


def inserir_endereco(endereco: Endereco) -> Endereco:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(INSERT_ENDERECO, 
            (endereco.logradouro, endereco.numero, endereco.complemento, endereco.bairro, endereco.cidade, endereco.estado, endereco.cep))
        endereco.id = cursor.lastrowid
        return endereco

def atualizar_endereco(endereco: Endereco) -> bool:

    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(UPDATE_ENDERECO, 
            (endereco.logradouro, endereco.numero, endereco.complemento, endereco.bairro, endereco.cidade, endereco.estado, endereco.cep, endereco.id))
        return (cursor.rowcount > 0)

def excluir_endereco(id: int) -> bool:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(DELETE_ENDERECO, (id,))
        return (cursor.rowcount > 0)

def obter_endereco_por_id(id: int) -> Endereco:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(GET_ENDERECO_BY_ID, (id,))
        resultado = cursor.fetchone()
        conexao.close()
        if resultado:
            return Endereco(*resultado)
        return None

def obter_enderecos_por_pagina(limite: int, offset: int) -> list[Endereco]:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(GET_ENDERECOS_BY_PAGE, (limite, offset))
        resultados = cursor.fetchall()
        conexao.close()
        return [Endereco(*resultado) for resultado in resultados]