condicoes_validas = ["A Fazer", "Em Progresso", "Feitos", "Obstruidos"]

class Tarefa:
    def __init__(eu, titulo, detalhes="", condicao="A Fazer", id = None):
        eu.id = id
        eu.titulo = titulo
        eu.detalhes = detalhes
        eu.condicao = condicao
    
    def para_dicionario(eu):
        return{
            "id": eu.id,
            "titulo": eu.titulo,
            "detalhes": eu.detalhes,
            "status": eu.condicao
        }
