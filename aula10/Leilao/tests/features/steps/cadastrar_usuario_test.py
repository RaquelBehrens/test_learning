import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from behave import *
from src.mercado_leilao import MercadoLeilao


# use_step_matcher("re")


@given('O nome de usuario {nome_usuario}')
def step_impl(context, nome_usuario):
    context.nome_usuario = nome_usuario


@given('o endereco {endereco_usuario}')
def step_impl(context, endereco_usuario):
    context.endereco_usuario = endereco_usuario


@given('o CPF {cpf_usuario}')
def step_impl(context, cpf_usuario):
    context.cpf_usuario = cpf_usuario


@given('o e-mail {email_usuario}')
def step_impl(context, email_usuario):
    context.email_usuario = email_usuario


@when('O usuario eh cadastrado')
def step_impl(context):
    context.mercado = MercadoLeilao()
    context.mercado.cadastra_usuario(context.nome_usuario, context.endereco_usuario,
    context.email_usuario, context.cpf_usuario)


@then('O sistema deve possuir usuarios')
def step_impl(context):
    assert context.mercado.possui_usuario() == True
