document.addEventListener("DOMContentLoaded",  function(){
    // let changeButton = document.getElementById("basketButton")
    // let defineId = document.getElementById("Idpro").value
    let proSection = document.getElementById('mainproduct')
    async function ProductsDetailed(){
        console.log('here');
        let response = await fetch(`/api/products/<int:pk>/`, {
            
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                // 'Authorization': `Bearer ${localStorage.getItem('token')}`
                },
            method: "GET",
            
        });
        let data = await response.json()
        console.log('product datadan qayidanlar :  ',data);
        
        
        let ids = data[i]['id']
            
        proSection.innerHTML = `
            <h4>${data['title']}</h4>
            <span class="price" id="priceItem" data-value="${data['value']}"><small>$</small>{{ pp.price }}</span> 
            Sale Tags
            <div class="on-sale"> 10% <span>OFF</span> </div>
            <ul class="item-owner">
                <li>Designer :<span> ${ data['product']['category']['name'] }</span></li>
                <li>Brand:<span>${ [data]['product']['brand']['name'] }</span></li>
            </ul>
        `
        
         
    }
    ProductsDetailed();
    
});


