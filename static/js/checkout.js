document.addEventListener("DOMContentLoaded",  function(){
    let eachcard = document.getElementById('shippingpro')
    // let maxcount = document.getElementById("countStock");
    // let maxnumber = maxcount.getAttribute('max')
    // console.log(maxnumber);
    async function rendershipping(){
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
        
        let total_price = 0
        let totalItems = 0
        for (let i = 0; i < data.length; i++) {
            if (data[i]['count'] > 0 && data[i]['basket']['status']==false) {

                totalItems += parseInt(data[i]['count'])
                let ids = data[i]['id']
                total_price += parseFloat(data[i]['count'] * data[i]['price'])
                eachcard.innerHTML += `
                    <p>${data[i]['productVersion']['title']}   <span></span> <span> ----------------------- $   ${data[i]['price']} </span></p>
                    
                `
            }
            
            
        };
        let valueTotal = document.getElementById('totalOFshipment')
        valueTotal.innerHTML = `<p class="all-total">TOTAL COST <span> $ ${total_price.toFixed(2)}</span></p>`

    }
    rendershipping();
    
});


