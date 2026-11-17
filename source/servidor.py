from flask import Flask, jsonify, request
from source.tarefa import Tarefa, condicoes_validas
from source import gestor

#LEMBRETE: python -m source.servidor é o codigo a se rodar no terminal para subir.

site = Flask(__name__)
site.json.ensure_ascii = False
#Lembrando: 2xx = deu certo, 3xx = redirecionamento, 4xx = erro de input do usuario, 5xx = erro do sistema, não troca as bolas para não confundir o usuario.
@site.route("/tarefas", methods=["POST"])
def criar_tarefa():
    info = request.get_json(silent=True) or {}
    titulo = str(info.get("titulo","")).strip()
    if not titulo:
        return jsonify({"erro":"Bad Request. Por favor, insira um titulo!"}), 400
    status = info.get("status", "A Fazer")
    if status not in condicoes_validas:
        return jsonify({"erro":"Bad Request. Status de tarefa invalido!"}), 400
    
    nova_tarefa = Tarefa(titulo, info.get("detalhamento", ""), status) 
    gestor.add(nova_tarefa)
    return jsonify(nova_tarefa.para_dicionario()), 201

@site.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify([t.para_dicionario() for t in gestor.listar()])

@site.route("/tarefas/<int:id>", methods=["GET"])
def buscar_tarefa(id):
    tarefa = gestor.buscar(id)
    if tarefa is None:
        return jsonify({"erro": "Tarefa inexistente."}), 404
    return jsonify(tarefa.para_dicionario())

@site.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id): 
    info = request.get_json(silent=True) or {}
    titulo = str(info.get("titulo", "")).strip()
    if not titulo:
        return jsonify({"erro": "Por favor, insira um titulo valido!"}), 400
    status = info.get("status", "A Fazer")
    if status not in condicoes_validas:
        return jsonify({"erro": "Status de tarefa não valido!"}), 400
    tarefa = gestor.atualizar(id, titulo, info.get("detalhamento", ""), status)
    if tarefa is None:
        return jsonify({"erro": "Não foi possivel encontrar a tarefa, confira se digitou corretamente."}), 404
    return jsonify(tarefa.para_dicionario())

@site.route("/tarefas/<int:id>", methods=["DELETE"])
def apagar_tarefa(id):
    if gestor.remove(id):
        return "", 204
    return jsonify({"erro": "Tarefa não achada."}), 404

if __name__ == "__main__":
    site.run(debug=True)
