let num= document.querySelectorAll('.inputs').length
document.querySelectorAll('.inputs').forEach((input, index)=>{
    input.id=`input-${index + 1}`;
});
function Atualizar_tempo() {
    fetch('/tempo_restante')  // Faz uma requisição para obter o tempo restante
    .then(response => response.json())  // Converte a resposta para JSON
    .then(data => {
        // Verifica se o tempo chegou a zero
        if (data.tempo_restante_em_segundos <= 0) {
            // Redireciona para a próxima pergunta
            return window.location.href = '/quiz'; // Sai da função
        }

        // Calcula minutos e segundos a partir do tempo restante em segundos
        let minutos = Math.floor(data.tempo_restante_em_segundos / 60);
        let segundos = Math.floor(data.tempo_restante_em_segundos % 60);
        
        // Adiciona um zero à esquerda se os segundos forem menores que 10
        if (segundos < 10 && segundos >= 0) {
            segundos = '0' + segundos;
        }

        // Atualiza o conteúdo do elemento com o tempo restante
        let tempo_restante_elemento = document.getElementById('Tempo_restante');
        tempo_restante_elemento.innerHTML = `${minutos}:${segundos}`;
        tempo_restante_elemento.innerText = minutos + ':' + segundos; 

        // Chama a função novamente após 1 segundo
        setTimeout(Atualizar_tempo, 1000);
    })
    .catch(error => {
        console.error('Erro ao buscar o tempo restante:', error);
    });
}

// Inicia a atualização do tempo
Atualizar_tempo();

// Intercepta a navegação para voltar à página anterior
// Verifica se o usuário está navegando para trás
// Adiciona um estado inicial à história
window.history.pushState(null, document.title, window.location.href);

// Escuta mudanças no histórico (navegação)
window.addEventListener('popstate', function (event) {
    const abandonQuiz = confirm('Você deseja realmente abandonar o quiz?');
    if (abandonQuiz) {
        // Se o usuário confirmar, redirecione
        window.location.href = '/fases_quiz'; // Redirecione para a página de fases
    } else {
        // Caso contrário, reverte a navegação
        // Adiciona novamente o estado à história para evitar sair da página
        window.history.pushState(null, document.title, window.location.href);
    }
});

// Para garantir que o estado inicial permaneça ao recarregar a página
window.addEventListener('load', function() {
    window.history.replaceState(null, document.title, window.location.href);
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
