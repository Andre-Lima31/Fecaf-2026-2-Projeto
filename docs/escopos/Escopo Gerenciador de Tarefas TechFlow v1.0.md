# Projeto TrilhaFlow: v1.0

## Justificativa de Projeto: 
o cliente, uma startup de logística, lida com diversos processos e projetos simultaneamente, que são feitos de partes diferentes que devem ser concluídas para formar o projeto final, e cada uma dessas partes são manuseadas por equipes diferentes, e com frequência o progresso de cada projeto individual pode não ficar claro tanto para os participantes do próprio projeto, quanto para os gerentes e clientes que esperam a conclusão do projeto.

## Finalidade do Projeto: 
Organizar e dar visibilidade ao progresso individual de cada projeto e suas partes, permitindo que os gerentes e clientes possam acompanhar o progresso sem depender de relatos informais ou emails longos. Apresentando informação de maneira visual e intuitiva. 

## Descrição do Projeto: 
Sistema web de gerenciamento de tarefas em Kanban, desenvolvido pela TechFlow Solutions para uma startup de logística.

## Estimativa de Tempo Para Primeira Entrega: 
Duas sprints de 7 dias (uma semana), para o total de duas semanas.
Discussão entre cliente e TechFlow, levantamento de requisitos: 11/11/2026
Inicialização formal do projeto : 13/11/2026
Entrega esperada da primeira sprint: 20/11/2026

## Funcionalidades Incluídas:
- Criar, listar, editar e apagar tarefas (CRUD).
- Cada tarefa tem título (obrigatório), descrição e status.
- Status permitido: A Fazer, Em Progresso, Feito e Obstruído.
- Visualização das tarefas em colunas por status.
- Validação de entradas (título obrigatório, status válido).
- Testes automatizados e integração contínua (GitHub Actions).

## Exclusões da Versão 1.0:
- Prioridade das tarefas.
- Prazo (data limite) e alerta de atraso.
- Responsável pela tarefa.
- Painel de desempenho da equipe.
- Login e controle de usuários.
- Confirmação antes de apagar uma tarefa.

## Tecnologias Usadas: 
Python 3.8, Flask, Pytest, GitHub Actions. Interface em HTML, CSS e JavaScript, executados no navegador.
