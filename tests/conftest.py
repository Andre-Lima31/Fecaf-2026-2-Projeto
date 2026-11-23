import pytest

from source import gestor
from source.servidor import site


@pytest.fixture(autouse=True)
def limpar_gestor():
    gestor._tarefas.clear()
    gestor._atualID = 1


@pytest.fixture
def cliente():
    site.config["TESTING"] = True
    return site.test_client()


@pytest.fixture
def admin(cliente):
    cliente.post("/login", json={"nome": "gerente", "senha": "admin123"})
    return cliente
# Meio que uma gambiarra, esse é o cliente gerente já cadastrado com papel de gerente e permissões, já que sem os
# testes antigos como os de criação, alteração e exclusão sempre retornaram "401 Unauthorized" já que precisa
# do papel de gerente para fazer isso agora. Não mexer nisso.
