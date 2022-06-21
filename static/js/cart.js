document.addEventListener("DOMContentLoaded",  function(){
    // let changeButton = document.getElementById("basketButton")
    // let defineId = document.getElementById("Idpro").value
    let proSection = document.getElementById('basketUl')
    async function renderProducts(){
        console.log('here');
        let response = await fetch(`/api/basketitems/`, {
            
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
                },
            method: "GET",
            
        });
        let data = await response.json()
        console.log('datadan qayidanlar :  ',data);
        
        let total_price = 0
        let totalItems = 0
        for (let i = 0; i < data.length; i++) {
            if (data[i]['count'] > 0 && data[i]['basket']['status']==false) {
                // console.log(data[i]['productVersion']['id'], 've', defineId);
                // if (data[i]['productVersion']['id'] == defineId){
                    
                //     changeButton.innerHTML = `<a href="{% url 'home' %}" class="btn">GO TO CART</a>`

                // }else if(data[i]['productVersion']['id'] != defineId || totalItems==0){
                //     changeButton.innerHTML = `<a href="#." class="btn">ADD TO CART</a>`
                // }

                totalItems += parseInt(data[i]['count'])
                let ids = data[i]['id']
                // console.log('salam', data[i]['basket']['status']);
                total_price += parseFloat(data[i]['count'] * data[i]['price'])
                proSection.innerHTML += `
                <li >
                    <input type="hidden" value="${ids}" id="idd">
                    <div class="media-left">
                        <div class="cart-img"> <a href="#"> <img class="media-object img-responsive" src="${data[i]['productVersion']['image'][0]}" alt="..."> </a> </div>
                    </div>
                    <div class="media-body">
                    <h6 class="media-heading">${data[i]['productVersion']['product']['brand']['name']}</h6>
                    <span class="price"  data-value="{{ data[i].price }}">${data[i]['price']}</span><span id="priceItemm${ data[i].id }" class="qty" id="priceCount" data-value="{{ data[i].count }}"> ${data[i]['count']} <button onclick="plus(${data[i]['productVersion'].id}, ${ data[i].id }, ${ data[i].count}, ${ data[i].price } )" id="plus">+</button> <button onclick="minus(${data[i]['productVersion'].id}, ${ data[i].id }, ${ data[i].count}, ${ data[i].price } )" id="minus"> - </button> </span>
                    <span class="totall" id="finalPrice">Total price ${(data[i]['price'] * data[i]['count']).toFixed(2)}</span>
                    </div>
                </li>
                `
            }
            
        };
        if (totalItems > 0){
            document.getElementById('itemnumBer').innerHTML = totalItems;

        }
        
        
        let subTotal = document.getElementById('sub_price')
        subTotal.innerHTML = `
        <h5 class="text-center">SUBTOTAL: ${total_price.toFixed(2)}</h5>
        `
        
        
    }
    renderProducts();
    
});


