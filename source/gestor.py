# nota: o _ é para dizer que é uma variavel/tufla/valor interno, NÃO é para remover de novo.
_tarefas = []
_atualID = 1


def add(tarefa):
    # o global é necessario, se não ele acha que estamos redefinindo o _atualID, já que esta dentro de uma
    # função. Confuso, mas manter assim.
    global _atualID
    tarefa.id = _atualID
    _atualID += 1
    _tarefas.append(tarefa)
    return tarefa


def buscar(id):
    for tarefa in _tarefas:
        if tarefa.id == id:
            return tarefa
    return None


def listar():
    return _tarefas


def atualizar(id, titulo, detalhes, status):
    tarefa = buscar(id)
    if tarefa is None:
        return None
    tarefa.titulo = titulo
    tarefa.detalhes = detalhes
    tarefa.condicao = status
    return tarefa


def remove(id):
    selecionada = buscar(id)
    if not selecionada:
        return False
    else:
        _tarefas.remove(selecionada)
        return True
