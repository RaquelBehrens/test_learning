## Verificar coverage

`coverage run -m unittest discover -s tests`
`coverage html`

## Lista de Histórias

## Lista de Testes

- Teste 1: Criação de empresa: Empresa()
- Teste 2: Cadastrar funcionário: Empresa.cadastrarFuncionario()
- Teste 3: Não cadastrar funcionário com nome inválido: Empresa.cadastrarFuncionario()
- Teste 4: Não cadastrar funcionário com CPF inválido: Empresa.cadastrarFuncionario() e Empresa.\_\_validaCPF()
- Teste 5: Não cadastrar funcionário com cargo inválido: Empresa.cadastrarFuncionario()
- Teste 6: Não cadastrar funcionário com salário inválido: Empresa.cadastrarFuncionario()
- Teste 7: Cadastrar mais de um funcionário: Empresa.cadastrarFuncionario()
- Teste 8: Não cadastrar funcionário que já está cadastrado: Empresa.cadastrarFuncionario()
- Teste 9: Encontrar funcionário registrado na empresa: Empresa.encontrarFuncionario()
- Teste 10: Não encontrar funcionário não registrado na empresa: Empresa.encontrarFuncionario()
- Teste 11: Criar projeto sem equipe: Empresa.novoProjeto()
- Teste 12: Criar projeto com equipe de funcionários registrados na empresa: Empresa.novoProjeto()
- Teste 13: Não criar projeto com equipe que possui algum funcionário que não está registrado na empresa: Empresa.novoProjeto()
- Teste 14: Encontrar projeto registrado: Empresa.encontrarProjeto()
- Teste 15: Não encontrar projeto que não foi registrado: Empresa.encontrarProjeto()
- Teste 16: Insere funcionário em projeto: Empresa.adicionarAoProjeto()
- Teste 17: Não insere funcionário que não foi registrado em projeto: Empresa.adicionarAoProjeto()

- Teste 18: Criação de funcionário: Funcionario()

- Teste 19: Criação de projeto: Projeto()
