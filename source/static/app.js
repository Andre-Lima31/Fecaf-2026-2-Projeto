let idEmEdicao = null;

function iniciarEdicao(tarefa) {
    idEmEdicao = tarefa.id;
    document.getElementById("titulo").value = tarefa.titulo;
    document.getElementById("detalhes").value = tarefa.detalhes;
    document.getElementById("status").value = tarefa.status;
    document.getElementById("botao-enviar").textContent = "Atualizar";
}

async function apagarTarefa(tarefa) {
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
        cartao.appendChild(botaoEditar);
        cartao.appendChild(botaoApagar);
        
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

carregarTarefas(); //se remover isso daqui o codigo não é executado quando abre

//*E comentarios é com // no javascript por sinal, pois sei que vai demorar para se acostumar
