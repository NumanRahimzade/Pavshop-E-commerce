document.addEventListener("DOMContentLoaded",  function(){
    let eachcard = document.getElementById('cartUl')
    // let maxcount = document.getElementById("countStock");
    // let maxnumber = maxcount.getAttribute('max')
    // console.log(maxnumber);
    async function renderitemcard(){
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
                    if (data[i]['size']==value) {
                        var newsize = key
                        data[i]['size'] = newsize
                    }else{
                        data[i]['size']=data[i]['size']
                    }
                    
                }

                totalItems += parseInt(data[i]['count'])
                let ids = data[i]['id']
                total_price += parseFloat(data[i]['count'] * data[i]['price'])
                eachcard.innerHTML += `
                    <li class="col-sm-6">
                        <div class="row"> 
                            <!-- Media Image -->
                            <div class="col-sm-4"> <a href="#." class="item-img"> <img class="media-object" src="${data[i]['productVersion']['image'][0]}" alt=""> </a> </div>
                            
                            <!-- Item Name -->
                            <div class="col-sm-6" style="margin-top:85px;">
                                <div class="position-center-center">
                                    <h5>${data[i]['productVersion']['product']['brand']['name']}</h5>
                                    <p>${data[i]['productVersion']['title']}</p>
                                </div>
                            </div>
                            <div class="col-sm-2" style="margin-top:55px;">
                                <h5>${data[i]['size']}</h5>
                            </div>
                        </div>
                    </li>
                    
                    <!-- PRICE -->
                    <li class="col-sm-2">
                        <div class="position-center-center"> <span class="price"><small>$</small>${data[i]['price']}</span> </div>
                    </li>
                
                    <!-- QTY -->
                    <li class="col-sm-1">
                        <div class="position-center-center">
                            <div class="quinty"> 
                            <!-- QTY -->
                            <span id="priceItemm${ data[i].id }" class="qty" id="priceCount" data-value="{{ data[i].count }}"> ${data[i]['count']} <button onclick="plus(${data[i]['productVersion'].id}, ${ data[i].id }, ${ data[i].count}, ${ data[i].price }, ${data[i].newsize} )" id="plus">+</button> <button onclick="minus(${data[i]['productVersion'].id}, ${ data[i].id }, ${ data[i].count}, ${ data[i].price }, ${data[i].newsize} )" id="minus"> - </button> </span>
                            </div>
                        </div>
                    </li>
                
                    <!-- TOTAL PRICE -->
                    <li class="col-sm-2">
                        <div class="position-center-center"> <span class="price"><small>$</small><span class="totall" id="finalPrice">${(data[i]['price'] * data[i]['count']).toFixed(2)}</span></span> </div>
                    </li>
                    <li class="col-sm-1">
                        <div class="position-center-center"> <a href="#."><i class="icon-close" onclick="deleteitem(${ data[i].id })" id="delitem"></i></a> </div>
                    </li>
                `
                let Total = document.getElementById('tot_price')
                Total.innerHTML += `
                
                <p>${data[i]['productVersion']['product']['brand']['name']}<span>$${(data[i]['price'] * data[i]['count']).toFixed(2)}</span></p>
                      
                `
            }
            
            
        };
        
        let valueTotal = document.getElementById('finalprice')
        valueTotal.innerHTML = `<h5 class="text-center">TOTAL COST $: ${total_price.toFixed(2)}</h5>`
        
    }
    renderitemcard();
    
});


