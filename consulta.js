async function mostrarProdutos(){
    const apiUrl = "http://127.0.0.1/getall"
    let dados = []
    try{
       const consulta = await fetch(apiUrl)
       console.log(consulta)
       dados = await consulta.json()
       console.log(dados)
       atualizaLista(dados)
       //atualizaLista(dados)
       if (!consulta.ok){
        console.log("A API não está respondendo")
       }
        
    }catch(error){
    console.error("Erro ao buscar informações", error)
    }
}
function atualizaLista(){
    let produtos = document.getElementById("produtos")
    produtos.innerHTML = ""
    for (let i of dados){
        produtos.innerText += `Produto: ${i.nome}`
    }
}
function atualizaLista(dados){
    let produtos = document.getElementById("produto")
    produtos.innerHTML = ""
    for (let i of dados){
        produtos.innerHTML += `
        <div class="col-12 col-sm-6 col-md-4  colcol-lg-3">
        <div class="card" style="background-color:#ECDCCB;">
        <img src="place.avif" class="card-img-top" style="background-color:#ECDCCB;">
        <div class="card-body text-center" style="background-color:#ECDCCB;">
            <h5 class="card-title">${i.nome}</h5>
            <p class="card-text">${i.descricao}</p>
            <a href="#" class="btn">${i.preco}</a>
        </div>
        </div>
        `
    }
}