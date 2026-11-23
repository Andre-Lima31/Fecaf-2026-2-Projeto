let idEmEdicao = null;
let papelAtual = null;

function iniciarEdicao(tarefa) {
    idEmEdicao = tarefa.id;
    document.getElementById("titulo").value = tarefa.titulo;
    document.getElementById("detalhes").value = tarefa.detalhes;
    document.getElementById("status").value = tarefa.status;
    document.getElementById("botao-enviar").textContent = "Atualizar";
}

async function apagarTarefa(tarefa) {
    if (!confirm('Apagar a tarefa "' + tarefa.titulo + '"?')) {
        return;
    }
    const resposta = await fetch("/tarefas/" + tarefa.id, { method: "DELETE" });

    if (resposta.ok) {
        if (idEmEdicao === tarefa.id) {
            idEmEdicao = null;
            document.getElementById("formulario").reset();
            document.getElementById("botao-enviar").textContent = "Adicionar";
        }
        carregarTarefas();
    } else {
        const erro = await resposta.json();
        document.getElementById("mensagem-erro").textContent = erro.erro;
    }
}

async function carregarTarefas() {
    const resposta = await fetch("/tarefas");
    const ListaDeTarefas = await resposta.json();

    document.querySelectorAll(".coluna").forEach(function (coluna) {
        coluna.innerHTML = "";
    });

    ListaDeTarefas.forEach(function (tarefa) {
        const coluna = document.querySelector(
            '.coluna[data-status="' + tarefa.status + '"]'
        );
        if (!coluna) {
            return;
        }

        const cartao = document.createElement("div");
        cartao.className = "cartao";
        const titulo = document.createElement("strong");
        titulo.textContent = tarefa.titulo;
        const detalhes = document.createElement("p");
        detalhes.textContent = tarefa.detalhes;

        const botaoEditar = document.createElement("button");
        botaoEditar.textContent = "Editar";
        botaoEditar.addEventListener("click", function () {
        iniciarEdicao(tarefa);

    });
        const botaoApagar = document.createElement("button");
        botaoApagar.textContent = "Excluir";
        botaoApagar.addEventListener("click", function () {
        apagarTarefa(tarefa);});
        cartao.appendChild(titulo);
        cartao.appendChild(detalhes);
        coluna.appendChild(cartao);
        if (papelAtual === "gerente") {
            cartao.appendChild(botaoEditar);
            cartao.appendChild(botaoApagar);
        }
        
    });
}

document.getElementById("formulario").addEventListener("submit", async function (evento) {
    evento.preventDefault(); 

    const url = idEmEdicao === null ? "/tarefas" : "/tarefas/" + idEmEdicao;
    const metodo = idEmEdicao === null ? "POST" : "PUT";

    const resposta = await fetch(url, {
        method: metodo,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            titulo: document.getElementById("titulo").value,
            detalhes: document.getElementById("detalhes").value,
            status: document.getElementById("status").value
        })
    });

    const mensagem = document.getElementById("mensagem-erro");
    if (resposta.ok) {
        mensagem.textContent = "";
        document.getElementById("formulario").reset();
        idEmEdicao = null;
        document.getElementById("botao-enviar").textContent = "Adicionar";
        carregarTarefas();  
    } else {
        const erro = await resposta.json();
        mensagem.textContent = erro.erro; 
    }
});

function mostrarTela(logado) {
    document.getElementById("tela-login").style.display = logado ? "none" : "block";
    document.getElementById("app").style.display = logado ? "block" : "none";
}

async function verificarSessao() {
    const resposta = await fetch("/sessao");
    if (resposta.ok) {
        const usuario = await resposta.json();
        document.getElementById("usuario-logado").textContent =
            usuario.nome + " (" + usuario.papel + ")";
        mostrarTela(true);
        papelAtual = usuario.papel;
        document.getElementById("formulario").style.display =
            papelAtual === "gerente" ? "block" : "none";
        carregarTarefas();
    } else {
        mostrarTela(false);
    }
}

document.getElementById("form-login").addEventListener("submit", async function (evento) {
    evento.preventDefault();
    const resposta = await fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            nome: document.getElementById("login-nome").value,
            senha: document.getElementById("login-senha").value
        })
    });
    if (resposta.ok) {
        document.getElementById("form-login").reset();
        document.getElementById("login-erro").textContent = "";
        verificarSessao();
    } else {
        const erro = await resposta.json();
        document.getElementById("login-erro").textContent = erro.erro;
    }
});

document.getElementById("botao-sair").addEventListener("click", async function () {
    await fetch("/logout", { method: "POST" });
    mostrarTela(false);});

verificarSessao(); //agora isso só vai rodar se a resposta para o login voltar como ok, else não carrega.

//*E comentarios é com // no javascript por sinal, pois sei que vai demorar para se acostumar
