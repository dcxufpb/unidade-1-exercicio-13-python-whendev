# coding: utf-8

import cupom
import pytest
from datetime import datetime

def verifica_campo_obrigatorio_objeto(mensagem_esperada, Venda):
  with pytest.raises(Exception) as excinfo:
    Venda.imprime_cupom()
  the_exception = excinfo.value
  assert mensagem_esperada == str(the_exception)

# Todas as variaveis preenchidas

DATA_HORA_VENDA = datetime(2020, 11, 25, 10, 30, 40)
CCF = "021784"
COO = "035804"


NOME_LOJA = "Loja 1"
LOGRADOURO = "Log 1"
NUMERO = 10
COMPLEMENTO = "C1"
BAIRRO = "Bai 1"
MUNICIPIO = "Mun 1"
ESTADO = "E1"
CEP = "11111-111"
TELEFONE = "(11) 1111-1111"
OBSERVACAO = "Obs 1"
CNPJ = "11.111.111/1111-11"
INSCRICAO_ESTADUAL = "123456789"


ENDERECO_COMPLETO = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO,
                                   MUNICIPIO, ESTADO, CEP)

LOJA_COMPLETA = cupom.Loja(NOME_LOJA, ENDERECO_COMPLETO, TELEFONE, OBSERVACAO,
                           CNPJ, INSCRICAO_ESTADUAL)

VENDA_COMPLETA = LOJA_COMPLETA.vender(DATA_HORA_VENDA, CCF, COO)

TEXTO_ESPERADO_CUPOM_FISCAL = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789
------------------------------
25/11/2020 10:30:40V CCF:021784 COO: 035804'''

def test_venda_completa():
    assert (
        VENDA_COMPLETA.imprime_cupom() == TEXTO_ESPERADO_CUPOM_FISCAL
    )


MENSAGEM_DATAHORA_OBRIGATORIO = "O campo data da venda é obrigatório"

ENDERECO_COMPLETO = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO,
                                   MUNICIPIO, ESTADO, CEP)

LOJA_COMPLETA = cupom.Loja(NOME_LOJA, ENDERECO_COMPLETO, TELEFONE, OBSERVACAO,
                           CNPJ, INSCRICAO_ESTADUAL)

VENDA_DATAHORA_VAZIA = LOJA_COMPLETA.vender("", CCF, COO)

def test_valida_venda1():
    verifica_campo_obrigatorio_objeto(MENSAGEM_DATAHORA_OBRIGATORIO,
                                      VENDA_DATAHORA_VAZIA)


MENSAGEM_COO_OBRIGATORIO = "O campo coo da venda é obrigatório"

ENDERECO_COMPLETO = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO,
                                   MUNICIPIO, ESTADO, CEP)

LOJA_COMPLETA = cupom.Loja(NOME_LOJA, ENDERECO_COMPLETO, TELEFONE, OBSERVACAO,
                           CNPJ, INSCRICAO_ESTADUAL)

VENDA_COO_VAZIA = LOJA_COMPLETA.vender(DATA_HORA_VENDA, CCF, "")

def test_valida_venda2():
    verifica_campo_obrigatorio_objeto(MENSAGEM_COO_OBRIGATORIO,
                                      VENDA_COO_VAZIA)


MENSAGEM_CCF_OBRIGATORIO = "O campo ccf da venda é obrigatório"

ENDERECO_COMPLETO = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO,
                                   MUNICIPIO, ESTADO, CEP)

LOJA_COMPLETA = cupom.Loja(NOME_LOJA, ENDERECO_COMPLETO, TELEFONE, OBSERVACAO,
                           CNPJ, INSCRICAO_ESTADUAL)

VENDA_CCF_VAZIA = LOJA_COMPLETA.vender(DATA_HORA_VENDA, "", COO)

def test_valida_venda3():
    verifica_campo_obrigatorio_objeto(MENSAGEM_CCF_OBRIGATORIO,
                                      VENDA_CCF_VAZIA)
