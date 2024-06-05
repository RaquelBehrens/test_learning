import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from behave import *
from src.mercado_leilao import MercadoLeilao

@given(u'o cadastro do usuario {nome_usuario} foi realizado')
def step_impl(context, nome_usuario):
    context.mercado = MercadoLeilao()
    context.mercado.cadastra_usuario(nome_usuario, "Endereço", "Email", "055.761.919-00")
    context.nome_usuario = nome_usuario


@given(u'o nome do produto {nome_produto}')
def step_impl(context, nome_produto):
    context.nome_produto = nome_produto


@given(u'a descricao do produto {descricao_produto}')
def step_impl(context, descricao_produto):
    context.descricao_produto = descricao_produto


@given(u'e o lance {lance}')
def step_impl(context, lance):
    context.lance = lance


@given(u'e o cpf do leiloador {cpf_leiloador}')
def step_impl(context, cpf_leiloador):
    context.cpf_leiloador = cpf_leiloador


@when(u'cadastrar o produto')
def step_impl(context):
    try:
        context.mercado.cadastra_produto(context.nome_produto, context.descricao_produto, 
                                         context.lance, context.cpf_leiloador, 0)
        context.msg = 'Produto cadastrado com sucesso'
    except Exception as e:
        context.msg = e.__str__()


@then(u'o sistema cadastra com sucesso')
def step_impl(context):
    assert 'Produto cadastrado com sucesso' == context.msg


@given(u'sofa amarelo ja foi cadastrado')
def step_impl(context):
    context.mercado.cadastra_produto("sofa", "amarelo", 100, "055.761.919-00", 0)


@then(u'o sistema mostra a mensagem {mensagem}')
def step_impl(context, mensagem):
    assert mensagem == context.msg
