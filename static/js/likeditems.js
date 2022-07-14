document.addEventListener("DOMContentLoaded",  function(){
    // let changeButton = document.getElementById("basketButton")
    // let defineId = document.getElementById("Idpro").value
    let proSection = document.getElementById('likeditems')
    async function renderProducts(){
        console.log('here');
        let response = await fetch(`/api/wishlists/`, {
            
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
                },
            method: "GET",
            
        });
        let data = await response.json()
        console.log('basket datadan qayidanlar :  ',data);
        
        for (let i = 0; i < data.length; i++) {

            let ids = data[i]['productversion']['title']
            console.log('tezz', ids);
            proSection.innerHTML += `
            <li >
            <input type="hidden" value="${ids}" id="idd">
            <div class="media-left">
            <div class="cart-img"> <a href="#"> <img class="media-object img-responsive" src="${data[i]['productVersion']['image'][0]}" alt="..."> </a> </div>
            </div>
            <div class="media-body">
            <h6 class="media-heading">${data[i]['productVersion']['product']['brand']['name']}</h6>
            <span class = "size">size: ${data[i]['size']}</span>
            <span class="price"  data-value="{{ data[i].price }}">price: ${data[i]['price']}</span><span id="priceItemm${ data[i].id }" class="qty" id="priceCount" data-value="{{ data[i].count }}"> ${data[i]['count']} <button onclick="plus(${data[i]['productVersion'].id}, ${ data[i].id }, ${ data[i].count}, ${ data[i].price }, ${data[i].newsize} )" id="plus">+</button> <button onclick="minus(${data[i]['productVersion'].id}, ${ data[i].id }, ${ data[i].count}, ${ data[i].price}, ${data[i].newsize} )" id="minus"> - </button> </span>
            <span class="totall" id="finalPrice">Total price: ${(data[i]['price'] * data[i]['count']).toFixed(2)}</span>
            </div>
            </li>
            `
            
        };
    }
    renderProducts();
    
});


