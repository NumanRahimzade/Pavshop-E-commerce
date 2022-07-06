// let plusButton = document.getElementById("plus");
// console.log(plusButton);
async function plus(productVersion, valueId, countItem, priceItem, size) {
// let maxcount = document.getElementById("countStock");
// let maxnumber = maxcount.getAttribute('max')
// console.log(countItem, );  
// console.log(maxnumber, 'maximum');
    // if (countItem <= parseInt(maxnumber)){
        let postData = { 
            "productVersion": productVersion,
            "price": parseFloat(priceItem),
            "sub_total": parseFloat(priceItem),
            "count": parseInt(++countItem),
            "size": size,
        }
        // let newCount = countItem++;
        // document.querySelector(`#priceItemm${valueId}`).innerHTML = newCount;
        async function addProducts(){
            console.log('here');
            let response = await fetch(`http://localhost:8000/api/basketitems/${valueId}/`, {
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
        addProducts();
    // }
    

};
