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