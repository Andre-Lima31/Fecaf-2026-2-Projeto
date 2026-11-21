from source.tarefa import Tarefa


def test_dicionario():
    tarefa = Tarefa("Escrever README", "Versão inicial", "A Fazer", 1)
    assert tarefa.para_dicionario() == {
        "id": 1,
        "titulo": "Escrever README",
        "detalhes": "Versão inicial",
        "status": "A Fazer",
    }