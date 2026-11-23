from source import gestor
from source.tarefa import Tarefa


# Teste para verificar se o AtualID (para gerar um ID automaticamente sem uma inserção do proprio usuario)
# funciona corretamente. Se a primeira tarefa (a) tiver o ID 1 e a segunda tarefa (b) o ID 2: Passed.
def test_add():
    a = gestor.add(Tarefa("A"))
    b = gestor.add(Tarefa("B"))
    assert a.id == 1
    assert b.id == 2

# Teste de verificação da função buscar do gestor, ele cria uma tarefa A e então tenta a achar, caso retorne
#  o nome 'A' para a tarefa de ID 1: Passed


def test_buscar():
    gestor.add(Tarefa("A"))
    assert gestor.buscar(1).titulo == "A"
    assert gestor.buscar(99) is None

# Teste de verificação da função remover do gestor. Ele adiciona uma tarefa A com ID automatico 1 e roda a
# função remove, e então a função listar, se a lista retorna vazia: Passed


def test_remover():
    gestor.add(Tarefa("A"))
    assert gestor.remove(1) is True
    assert gestor.remove(1) is False
    assert gestor.listar() == []

# Teste de atualização, adiciona uma tarefa A de ID 1, e então roda a função atualizar, caso a tarefa que
# retorne seja condizente a tentativa de atualização: Passed.


def test_atualizar():
    gestor.add(Tarefa("A"))
    tarefa = gestor.atualizar(1, "B", "nova", "Feito")
    assert tarefa.titulo == "B"
    assert tarefa.condicao == "Feito"
    assert gestor.atualizar(99, "X", "", "A Fazer") is None
