document.addEventListener("DOMContentLoaded",  function(){
    let heart = document.getElementById('wishyou');
    heart.addEventListener('click', async (event) => {
        event.preventDefault();
        // let countItem = document.getElementById('countStock').value
        let size = document.getElementById('sizedefine').value
        let price = document.getElementById('priceItem')
        let priceItem = price.getAttribute("data-value")
        let findItem = document.getElementById('Idpro')
        let valueId = findItem.value
        let finduser = document.getElementById('Iduser')
        let userr = finduser.value
        console.log(userr, '++++++++');
        console.log('value-id: ',valueId);
        
        // let proSection = document.getElementById('basketUl')
        
        async function gethearts(){
            
            let postData = {
                
                "user": userr,
                "productversion": parseInt(valueId),
                
            
            }
            
            let response = await fetch('/api/wishlists/', {
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                },
                method: "POST",
                body: JSON.stringify(postData)
            });
            console.log('salam olsun');
        // window.location.reload()    
        }
        gethearts();        
    });
});