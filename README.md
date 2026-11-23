# Projeto TrilhaFlow v1.1

Sistema web de gerenciamento de tarefas em Kanban, desenvolvido pelaTechFlow Solutions para uma startup de logística.

## Objetivo
Dar visibilidade ao andamento de projetos e de suas partes, para equipes, gerentes e clientes acompanharem o progresso das tarefas em um quadro único.

## Escopo
Resumo da versão 1.1: criar, listar, editar e apagar tarefas, com título, descrição e status (A Fazer, Em Progresso, Feito e Obstruído), exibidas em colunas por status, sistema de login com senha*. O escopo completo está em O escopo completo está em `docs/escopo/Escopo Trilha Flow v1.1.md`..
*senhas usadas são ficticias.

## Metodologia de Trabalho
Kanban, com o quadro no GitHub Projects (aba Projects do repositório).
Colunas: To Do, In Progress, Done e Blockage (tarefas bloqueadas por
dependências externas, equivalente ao status "Obstruído" no TrilhaFlow).

Prioridades do backlog: 
**Prioridade Alta** = sem isso não se entrega ao cliente (ex.: sistema de login);
**Atenção** = equivalente a prioridade media, necessário primeiro devemos focar na prioridade alta (ex.: testes e verificação de qualidade).

## Tecnologias Usadas
Python 3.8, Flask, Pytest, Flake8, GitHub Actions. Interface em HTML, CSS e JavaScript, executados no navegador.

## Como executar
1. Clone o repositório e entre na pasta do projeto.
2. Crie e ative um ambiente virtual:
   - `python -m venv venv` (ou `python -m venv amb_virtu`, nome usado nos registros em `docs/`)
   - Windows: `venv\Scripts\activate` ou `amb_virtu\Scripts\activate`
3. Instale as dependências: `pip install -r requirements.txt`
4. Suba o servidor: `python -m source.servidor`
5. Abra no navegador o endereço exibido no terminal (por padrão, `http://127.0.0.1:5000`).

Testes: com o ambiente ativo, rode `pytest` na raiz do projeto.

## Estrutura do projeto
- `source/`: código do sistema (modelo, gestor, servidor, interface).
- `tests/`: testes automatizados.
- `docs/`: documentação, escopos, diagramas, prints de todo o processo separados em pastas por dia, `historico_commits` e requisições de teste da API.
