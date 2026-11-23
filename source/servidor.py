from flask import Flask, jsonify, request, render_template, session
from source.usuario import usuarios
from source.tarefa import Tarefa, condicoes_validas
from source import gestor

# LEMBRETE: python -m source.servidor é o codigo a se rodar no terminal para subir.

site = Flask(__name__)
site.secret_key = "chave-de-demonstração-trilhaflow"
site.json.ensure_ascii = False
# Lembrando: 2xx = deu certo, 3xx = redirecionamento, 4xx = erro de input do usuario, 5xx = erro do sistema.


@site.route("/tarefas", methods=["POST"])
def criar_tarefa():
    negado = exige_papel("gerente")
    if negado:
        return negado
    info = request.get_json(silent=True) or {}
    titulo = str(info.get("titulo", "")).strip()
    if not titulo:
        return jsonify({"erro": "Bad Request. Por favor, insira um titulo!"}), 400
    status = info.get("status", "A Fazer")
    if status not in condicoes_validas:
        return jsonify({"erro": "Bad Request. Status de tarefa invalido!"}), 400

    nova_tarefa = Tarefa(titulo, info.get("detalhes", ""), status)
    gestor.add(nova_tarefa)
    return jsonify(nova_tarefa.para_dicionario()), 201


@site.route("/tarefas", methods=["GET"])
def listar_tarefas():
    negado = exige_papel()
    if negado:
        return negado
    return jsonify([t.para_dicionario() for t in gestor.listar()])


@site.route("/tarefas/<int:id>", methods=["GET"])
def buscar_tarefa(id):
    negado = exige_papel()
    if negado:
        return negado
    tarefa = gestor.buscar(id)
    if tarefa is None:
        return jsonify({"erro": "Tarefa inexistente."}), 404
    return jsonify(tarefa.para_dicionario())


@site.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    negado = exige_papel("gerente")
    if negado:
        return negado
    info = request.get_json(silent=True) or {}
    titulo = str(info.get("titulo", "")).strip()
    if not titulo:
        return jsonify({"erro": "Por favor, insira um titulo valido!"}), 400
    status = info.get("status", "A Fazer")
    if status not in condicoes_validas:
        return jsonify({"erro": "Status de tarefa não valido!"}), 400
    tarefa = gestor.atualizar(id, titulo, info.get("detalhes", ""), status)
    if tarefa is None:
        return jsonify({"erro": "Não foi possivel encontrar a tarefa, confira se digitou corretamente."}), 404
    return jsonify(tarefa.para_dicionario())


@site.route("/tarefas/<int:id>", methods=["DELETE"])
def apagar_tarefa(id):
    negado = exige_papel("gerente")
    if negado:
        return negado
    if gestor.remove(id):
        return "", 204
    return jsonify({"erro": "Tarefa não achada."}), 404


@site.route("/")
def pagina_inicial():
    return render_template("index.html")


@site.route("/login", methods=["POST"])
def login():
    info = request.get_json(silent=True) or {}
    usuario = usuarios.get(info.get("nome", ""))
    if usuario is None or not usuario.conferir_senha(info.get("senha", "")):
        return jsonify({"erro": "Nome ou senha incorretos."}), 401  # significa Unauthorized
    session["nome"] = usuario.nome
    session["papel"] = usuario.papel
    return jsonify({"nome": usuario.nome, "papel": usuario.papel})


@site.route("/logout", methods=["POST"])
def logout():
    """Desligando."""
    session.clear()
    return "", 204


@site.route("/sessao", methods=["GET"])
def sessao():
    if "nome" not in session:
        return jsonify({"erro": "Faça login."}), 401
    return jsonify({"nome": session["nome"], "papel": session["papel"]})


def exige_papel(papel=None):
    if "nome" not in session:
        return jsonify({"erro": "Faça login."}), 401
    if papel is not None and session["papel"] != papel:
        return jsonify({"erro": "Sem permissão para esta ação."}), 403  # significa forbidden
    return None


if __name__ == "__main__":
    site.run(debug=True)
