document.addEventListener("DOMContentLoaded",  function(){
    let button = document.getElementById('basketButton');
    button.addEventListener('click', async (event) => {
        event.preventDefault();
        let countItem = document.getElementById('countStock').value
        let size = document.getElementById('sizedefine').value
        let price = document.getElementById('priceItem')
        let priceItem = price.getAttribute("data-value")
        let findItem = document.getElementById('Idpro')
        let valueId = findItem.value
        console.log('value-id: ',valueId);
        // let proSection = document.getElementById('basketUl')



        let weights = {
            'xxs':6, 
            'xs':7, 
            's':8, 
            'm':9, 
            'xl':10, 
            'xxl':11,
            'xxxl':12
          };
        for (let [key, value] of Object.entries(weights)) {
            if (size==key) {
                var newsize = value
                size = newsize
            }else{
                size=size
            }
            
        }
        
        
        async function getProducts(){
            
            let postData = {
                
                "productVersion": parseInt(valueId),
                "price": parseFloat(priceItem),
                "sub_total": parseFloat(priceItem),
                "count": parseInt(countItem),
                "size": size,
            
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