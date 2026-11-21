#Teste para verificar resultado CREATED (nº201):
def test_criar_tarefa(cliente):
    resposta = cliente.post("/tarefas", json={"titulo": "A", "detalhamento": "x"})
    assert resposta.status_code == 201
    assert resposta.get_json()["id"] == 1

#Teste para verificar um resultado OK (nº200):
def test_atualizar(cliente):
    cliente.post("/tarefas", json={"titulo": "A"})
    resposta = cliente.put("/tarefas/1", json={"titulo": "B", "status": "Feitos"})
    assert resposta.status_code == 200
    assert resposta.get_json()["status"] == "Feitos"

#Testes para verificar um resultado NOT FOUND (nº404):
def test_buscar_inexistente(cliente):
    assert cliente.get("/tarefas/99").status_code == 404

#Testes para verificar um resultado BAD REQUEST no caso do erro sem titulo (nº400):
def test_criar_sem_titulo(cliente):
    resposta = cliente.post("/tarefas", json={})
    assert resposta.status_code == 400

#Testes para verificar um resultado BAD REQUEST no caso de erro de status fora da lista (nº400):
def test_criar_status_invalido(cliente):
    resposta = cliente.post("/tarefas", json={"titulo": "A", "status": "Qualquer"})
    assert resposta.status_code == 400

#Teste para verificar um resultado NO CONTENT (nº204)
def test_apagar(cliente):
    cliente.post("/tarefas", json={"titulo": "A"})
    resposta = cliente.put("/tarefas/1", json={"titulo": "B", "status": "Feitos"})
    assert resposta.get_json()["titulo"] == "B"
    assert cliente.delete("/tarefas/1").status_code == 204
    assert cliente.delete("/tarefas/1").status_code == 404