document.addEventListener("DOMContentLoaded",  function(){
    let button = document.getElementById('basketButton');
    button.addEventListener('click', async (event) => {
        event.preventDefault();
        let countItem = document.getElementById('countStock').value
        let price = document.getElementById('priceItem')
        let priceItem = price.getAttribute("data-value")
        let findItem = document.getElementById('Idpro')
        let valueId = findItem.value
        console.log('value-id: ',valueId);
        // let proSection = document.getElementById('basketUl')
        async function getProducts(){
            
            let postData = {
                
                "productVersion": parseInt(valueId),
                "price": parseFloat(priceItem),
                "sub_total": parseFloat(priceItem),
                "count": parseInt(countItem),
            
            }
            
            let response = await fetch('/api/basketitems/', {
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                },
                method: "POST",
                body: JSON.stringify(postData)
            });
            // deyisiklik edile biler alt setre *******************
        window.location.reload()    
        }
        getProducts();        
    });
});