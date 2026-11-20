# Projeto TrilhaFlow v1.0

Sistema web de gerenciamento de tarefas em Kanban, desenvolvido pela TechFlow Solutions para uma startup de logística.

## Objetivo
Dar visibilidade ao andamento de projetos e de suas partes, para equipes,
gerentes e clientes acompanharem o progresso das tarefas em um quadro único.

## Escopo
Resumo da versão 1.0: criar, listar, editar e apagar tarefas, com título,
descrição e status (A Fazer, Em Progresso, Feito e Obstruído), exibidas em
colunas por status.
O escopo completo está em "docs/Escopo Gerenciador de Tarefas TechFlow v1.0.md"

## Metodologia de Trabalho
Kanban, com o quadro no GitHub Projects (aba Projects do repositório).
Colunas: To Do, In Progress, Done e Blockage (tarefas bloqueadas por dependências externas, equivalente ao status "Obstruído" no TrilhaFlow).

## Tecnologias Usadas
Python 3.8, Flask, Pytest, GitHub Actions. Interface em HTML, CSS e
JavaScript, executados no navegador.

## Como executar
1. Clone o repositório e entre na pasta do projeto.
2. Crie e ative um ambiente virtual:
   - `python -m venv venv` (o tradicional); ou `python -m venv amb_virtu` (como demonstrado nas recordações do historico_commits)
   - Windows: `venv\Scripts\activate`/`amb_virtu\Scripts\activate`
3. Instale as dependências: `pip install -r requirements.txt`
4. Suba o servidor: `python -m source.servidor`
5. Abra o caminho instrudo pelo terminal no navegador. (no projeto apareceu como "* Running on http://127.0.0.1:5000")

## Estrutura do projeto
- `source/`: código do sistema (modelo, gestor, servidor, interface).
- `tests/`: testes automatizados.
- `docs/`: documentação, diagramas, prints de todo o processo separado em dias, e requisições de teste da API.

## Mudança de escopo
(Esta seção será preenchida na reunião da sprint 1. Realizada em 19/11/2026 - 19:00 BRT)
