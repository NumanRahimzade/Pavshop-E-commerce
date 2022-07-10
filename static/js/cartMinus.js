let minusButton = document.getElementById("minus");
console.log(minusButton, 'salamm');
async function minus(productVersion, valueId, countItem, priceItem, size) {
    console.log('mius bura');
    
    // if (countItem.value < parseInt(countItem).getAttribute('max')){
    let postData = { 
        "productVersion": productVersion,
        "price": parseFloat(priceItem),
        "sub_total": parseFloat(priceItem),
        "count": parseInt(--countItem),
        "size": size,
    }
    // let newCount = countItem++;
    // document.querySelector(`#priceItemm${valueId}`).innerHTML = newCount;
    async function removeProducts(){
        console.log('here');
        let response = await fetch(`/api/basketitems/${valueId}/`, {
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            method: "PUT",
            body: JSON.stringify(postData)
        });
        // let data = await response.json()
        
        window.location.reload()
    }
    removeProducts();
    // }
    

};
