window.history.pushState(null, document.title, window.location.href);
window.addEventListener('popstate', function (event) {
    const abandonQuiz = confirm('Você deseja voltar a página inicial?');
    if (abandonQuiz) {
        // Se o usuário confirmar, permita que ele saia
        window.location.href = '/'; // Redirecione para a página de fases
    } else {
        // Caso contrário, reverte a navegação
        window.history.pushState(null, document.title, window.location.href);
    }
});


// Seleciona os elementos
const jogosButton = document.getElementById('jogos');
const botoesJogos = document.querySelector('.botoes-jogos');

// Variável para rastrear o estado de visibilidade
let isVisible = false;

// Adiciona um event listener para o clique
jogosButton.addEventListener('click', () => {
    isVisible = !isVisible; // Alterna o estado de visibilidade
    botoesJogos.style.display = isVisible ? 'flex' : 'none'; // Mostra ou esconde os botões
});
