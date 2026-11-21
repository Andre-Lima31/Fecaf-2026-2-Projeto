# Projeto TrilhaFlow

**versão:** v1.0 (em evolução para a v1.1)

## Justificativa de Projeto: 
o cliente, uma startup de logística, lida com diversos processos e projetos simultaneamente, que são feitos de partes diferentes que devem ser concluídas para formar o projeto final, e cada uma dessas partes são manuseadas por equipes diferentes, e com frequência o progresso de cada projeto individual pode não ficar claro tanto para os participantes do próprio projeto, quanto para os gerentes e clientes que esperam a conclusão do projeto.

## Finalidade do Projeto: 
Organizar e dar visibilidade ao progresso individual de cada projeto e suas partes, permitindo que os gerentes e clientes possam acompanhar o progresso sem depender de relatos informais ou emails longos. Apresentando informação de maneira visual e intuitiva. 

## Descrição do Projeto: 
Sistema web de gerenciamento de tarefas em Kanban, desenvolvido pela TechFlow Solutions para uma startup de logística.

## Estimativa de Tempo Para Entrega da versão 1.1: 
Entrega esperada ao cliente: 27/11/2026.
Entrega interna da versão funcional: 23/11/2026. Os dias restantes sãoreservados a revisão, testes adicionais e ajustes.

## Incluidos na Versão:
- Criar, listar, editar e apagar tarefas (CRUD).
- Cada tarefa tem título (obrigatório), descrição e status.
- Status permitido: A Fazer, Em Progresso, Feito e Obstruído.
- Visualização das tarefas em colunas por status.
- Validação de entradas (título obrigatório, status válido).
- Testes automatizados e integração contínua (GitHub Actions).
- **Novo:** Sistema de login (testado com usuarios pré-registrados).
- **Novo:** Sistema de controle de alteração de tarefas baseado em nivel de autoridade
- **Novo:** Confirmação antes de apagar uma tarefa.
- **Novo:** Verificação de qualidade de código (flake8) no CI.
- **Novo:** Polimento da aparência da interface (cores por status, mensagem de erro estilizada, espaçamento dos botões e nome TrilhaFlow)

## Exclusões da Versão 1.1:
- Prioridade das tarefas.
- Prazo (data limite) e alerta de atraso.
- Responsável pela tarefa.
- Painel de desempenho da equipe.
- Sistema de cadastros para usuarios novos.

## Tecnologias Usadas: 
Python 3.8, Flask, Pytest, Flake8, GitHub Actions. Interface em HTML, CSS e JavaScript, executados no navegador.
