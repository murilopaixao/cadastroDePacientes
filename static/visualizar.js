const campoData = document.querySelector('#dataRecibo');

campoData.addEventListener("focusin", () => {
    if (campoData.value == '') {
        const today = new Date();
        let dd = (today.getDate() < 10 ? '0' : '') + today.getDate();
        let MM = ((today.getMonth() + 1) < 10 ? '0' : '') + (today.getMonth() + 1);
        let year = today.getFullYear();
        campoData.value = dd + '/' + MM + '/' + year
        
    }
});