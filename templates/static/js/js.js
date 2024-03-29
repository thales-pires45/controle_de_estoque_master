//Função para exibir o total faturado.
function renderiza_total_vendido(url){
        fetch(url, {
            method: 'get',
        }).then(function(result){
            return result.json()
        }).then(function(data){
            document.getElementById('faturamento_vendido').innerHTML = data.total
        })
    }

//Função para exibir o total de entrada.
function renderiza_total_comprado(url){
        fetch(url, {
            method: 'get',
        }).then(function(result){
            return result.json()
        }).then(function(data){
            document.getElementById('faturamento_entrada').innerHTML = data.total
        })
    }

//Função para exibir o total o faturamento.
function renderiza_o_faturamento(url){
        fetch(url, {
            method: 'get',
        }).then(function(result){
            return result.json()
        }).then(function(data){
            document.getElementById('faturamento_total').innerHTML = data.total
        })
    }

//Função para gerar cores aleatórios:
function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }

    return [bg_color, border_color];

}

//Função para renderizar o gráfico de Entrada
function renderiza_entrada_mensal(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('entrada_mensal').getContext('2d');
        var cores_entrada_mensal = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: "Entrada",
                    data: data.data,
                    backgroundColor: cores_entrada_mensal[0],
                    borderColor: cores_entrada_mensal[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}

//Função para renderizar o gráfico de faturamento mensal:
function renderiza_faturamento_mensal(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('faturamento_mensal').getContext('2d');
        var cores_faturamento_mensal = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: "Faturamento",
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal[0],
                    borderColor: cores_faturamento_mensal[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}

//Produto mais vendido:
function renderiza_produtos_mais_vendidos(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('produtos_mais_vendidos').getContext('2d');
        var cores_produtos_mais_vendidos = gera_cor(qtd=6)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Produto',
                    data: data.data,
                    backgroundColor: cores_produtos_mais_vendidos[0],
                    borderColor: cores_produtos_mais_vendidos[1],
                    borderWidth: 1
                }]
            },
        });
    })
}

//Produto mais vendido:
function renderiza_produtos_mais_entraram(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('produtos_mais_entraram').getContext('2d');
        var cores_produtos_mais_entraram = gera_cor(qtd=6)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Produto',
                    data: data.data,
                    backgroundColor: cores_produtos_mais_entraram[0],
                    borderColor: cores_produtos_mais_entraram[1],
                    borderWidth: 1
                }]
            },
        });
    })
}