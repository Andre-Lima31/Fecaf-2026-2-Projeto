_tarefas = [] #nota: o _ é para dizer que é uma variavel/tufla/valor interno, NÃO é para remover de novo.
_atualID = 1

def add(tarefa):
    global _atualID #o global é necessario, se não ele acha que estamos redefinindo o _atualID, já que esta dentro de uma função. Confuso, mas manter assim.
    tarefa.id = _atualID
    _atualID +=1
    _tarefas.append(tarefa)
    return tarefa

def listar():
    return _tarefas
    print (tarefas)

def buscar(id):
    for tarefa in _tarefas:
        if tarefa.id == id:
            return tarefa
            print (i)
        else:
            None
    return None

def remove(id):
    selecionada = buscar(id)
    if not selecionada:
        return False
    else:
        _tarefas.remove(selecionada)
        return True
