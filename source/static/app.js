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
        const detalhe = document.createElement("p");
        detalhe.textContent = tarefa.detalhamento;


        cartao.appendChild(titulo);
        cartao.appendChild(detalhe);
        coluna.appendChild(cartao);
    });
}

document.getElementById("formulario").addEventListener("submit", async function (evento) {
    evento.preventDefault();
    const resposta = await fetch("/tarefas", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            titulo: document.getElementById("titulo").value,
            detalhamento: document.getElementById("detalhes").value,
            status: document.getElementById("status").value
        })
    });

    const mensagem = document.getElementById("mensagem-erro");
    if (resposta.ok) {
        mensagem.textContent = "";
        document.getElementById("formulario").reset();
        carregarTarefas();
    } else {
        const erro = await resposta.json();
        mensagem.textContent = erro.erro;
    }
});

carregarTarefas(); //se remover isso daqui o codigo não é executado quando abre

//*E comentarios é com // no javascript por sinal, pois sei que vai demorar para se acostumar
