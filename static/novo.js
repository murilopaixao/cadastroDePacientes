const INPUT_CEP = document.querySelector('#cep');
const endereco = document.querySelector('#endereco');
const bairro = document.querySelector('#bairro');
const cidade = document.querySelector('#cidade');
const estado = document.querySelector('#estado');


INPUT_CEP.addEventListener("blur", () => {
    let cep = INPUT_CEP.value;
    
    if (cep.length !== 8) {
        console.log('Retornando')
        return;        
    }

    fetch(`https://viacep.com.br/ws/${cep}/json/`)
        .then(resposta => resposta.json())
        .then(json => {
            endereco.value = json.logradouro;
            bairro.value = json.bairro;
            cidade.value = json.localidade;
            estado.value = json.uf;

        });

})