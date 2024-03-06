const campoData = document.querySelector('#dataRecibo');
let id = document.querySelector('#id');
let idPaciente = document.querySelector('#idPaciente');
let nome  = document.querySelector('#nome');
let nomePaciente = document.querySelector('#nomePaciente');

idPaciente.value = id.value;
nomePaciente.value = nome.value;

campoData.addEventListener("focusin", () => {
    if (campoData.value == '') {
        const today = new Date();
        let dd = (today.getDate() < 10 ? '0' : '') + today.getDate();
        let MM = ((today.getMonth() + 1) < 10 ? '0' : '') + (today.getMonth() + 1);
        let year = today.getFullYear();
        campoData.value = dd + '/' + MM + '/' + year
        
    }
});

function abrirModal(){
    new bootstrap.Modal("#modal1").show();
}