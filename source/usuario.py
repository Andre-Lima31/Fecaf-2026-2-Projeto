from werkzeug.security import generate_password_hash, check_password_hash


class Usuario:
    def __init__(eu, nome, senha, papel):
        eu.nome = nome
        eu.papel = papel  # a função da pessoa.
        eu.senha_hash = generate_password_hash(senha)

    def conferir_senha(eu, senha):
        return check_password_hash(eu.senha_hash, senha)


usuarios = {
    "gerente": Usuario("gerente", "admin123", "gerente"),
    "cliente": Usuario("cliente", "00000", "cliente")
}  # existe já que nessa versão não temos cadastros, só usuarios fixos.
