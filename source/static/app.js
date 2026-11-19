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

carregarTarefas(); //se remover isso daqui o codigo não é executado quando abre

//*E comentarios é com // no javascript por sinal, pois sei que vai demorar para se acostumar