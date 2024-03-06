const search = document.getElementById('search')
const pacientesList = document.getElementById('pacientesList')


search.addEventListener('keyup', () => {
    let expressao = search.value.toLowerCase();

    let linhas = pacientesList.getElementsByTagName('tr')
    for (let posicao in linhas) {
        if (true == isNaN(posicao)) {
            continue;
        }
        let conteudoDaLinha = linhas[posicao].innerHTML.toLowerCase();
        if (true == conteudoDaLinha.includes(expressao)) {
            linhas[posicao].style.display = '';
        } else {
            linhas[posicao].style.display = 'none';
        }
        
    }
})