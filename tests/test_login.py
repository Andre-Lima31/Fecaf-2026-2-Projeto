# Teste para verificar resultado OK (nº200), caso o usuario faça um login valido:
def test_login_valido(cliente):
    r = cliente.post("/login", json={"nome": "gerente", "senha": "admin123"})
    assert r.status_code == 200
    assert r.get_json()["papel"] == "gerente"

# Teste para verificar resultado UNAUTHORIZED (nº401), caso o usuario faça um login invalido:


def test_login_senha_errada(cliente):
    r = cliente.post("/login", json={"nome": "gerente", "senha": "errada"})
    assert r.status_code == 401

# Teste para verificar resultado UNAUTHORIZED (nº401), caso o usuario tente visualizar lista deslogado:


def test_sem_login_nao_acessa(cliente):
    assert cliente.get("/tarefas").status_code == 401

# Teste para verificar resultado OK (nº200), caso o usuario tente visualizar a lista logado:


def test_cliente_visualiza(cliente):
    cliente.post("/login", json={"nome": "cliente", "senha": "00000"})
    assert cliente.get("/tarefas").status_code == 200

# Teste para verificar resultado NOT AUTHORIZED (nº403), caso um usuario tente fazer uma requisição sem
# permissão


def test_cliente_nao_cria_edita_nem_apaga(cliente):
    cliente.post("/login", json={"nome": "cliente", "senha": "00000"})
    assert cliente.post("/tarefas", json={"titulo": "A"}).status_code == 403
    assert cliente.put("/tarefas/1", json={"titulo": "B"}).status_code == 403
    assert cliente.delete("/tarefas/1").status_code == 403
