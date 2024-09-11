let num= document.querySelectorAll('.inputs').length
document.querySelectorAll('.inputs').forEach((input, index)=>{
    input.id=`input-${index + 1}`;
});
function Atualizar_tempo() {
    fetch('/tempo_restante')  // Faz uma requisição para obter o tempo restante
    .then(response => response.json())  // Converte a resposta para JSON
    .then(data => {
        // Verifica se o tempo chegou a zero
        
        // Calcula minutos e segundos a partir do tempo restante em segundos
        let minutos = Math.floor(data.tempo_restante_em_segundos / 60);
        let segundos = Math.floor(data.tempo_restante_em_segundos % 60);
        
        // Adiciona um zero à esquerda se os segundos forem menores que 10
        if (segundos < 10 && segundos >= 0) {
            segundos = '0' + segundos;
        }
        if (data.tempo_restante_em_segundos <= 0) {
            // Redireciona para a próxima pergunta
            // Substitua pela rota correta
            return window.location.href = '/quiz'; // Sai da função
        }

        // Atualiza o conteúdo do elemento com o tempo restante
        let tempo_restante_elemento = document.getElementById('Tempo_restante');
        tempo_restante_elemento.innerHTML = `${minutos}:${segundos}`;
        tempo_restante_elemento.innerText = minutos + ':' + segundos; 
    });
}

// Atualiza o tempo restante a cada segundo
setInterval(Atualizar_tempo, 1000);

// Intercepta a navegação para voltar à página anterior
// Verifica se o usuário está navegando para trás
window.history.pushState(null, document.title, window.location.href);
window.addEventListener('popstate', function (event) {
    const abandonQuiz = confirm('Você deseja realmente abandonar o quiz?');
    if (abandonQuiz) {
        // Se o usuário confirmar, permita que ele saia
        window.location.href = '/fases_quiz'; // Redirecione para a página de fases
    } else {
        // Caso contrário, reverte a navegação
        window.history.pushState(null, document.title, window.location.href);
    }
});